import streamlit as st
import pandas as pd
import plotly.express as px

# URL for the Titanic dataset
titanic_url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'


def main():
    st.title("Interactive Data Analysis App")
    st.write("Upload a CSV file or use the Titanic dataset to get started")

    # File upload
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    load_titanic = st.checkbox("Use Titanic Dataset")

    if uploaded_file is not None or load_titanic:
        if load_titanic:
            df = pd.read_csv(titanic_url)
        else:
            df = pd.read_csv(uploaded_file)

        st.write("## Data")
        st.write(df)

        if st.checkbox("Show Summary Statistics"):
            st.write("## Summary Statistics")
            st.write(df.describe())

        if st.checkbox("Show Data Cleaning"):
            st.write("## Data Cleaning")
            missing_values = df.isnull().sum()
            st.write("### Missing Values")
            st.write(missing_values)
            
            fill_method = st.selectbox("Select method to fill missing values", ["Mean", "Median", "Mode"])
            column=st.selectbox("Choose Column",df.columns)
            if fill_method == "Mean":
                df[column] = df[column].fillna(df[column].mean())
            elif fill_method == "Median":
                df[column] = df[column].fillna(df[column].median())
            else:
                df[column] = df[column].fillna(df[column].mode().iloc[0])
            st.write("### Data after cleaning")
            st.write(df)

        if st.checkbox("Show Data Filtering"):
            st.write("## Data Filtering")
            column = st.selectbox("Select column to filter by", df.columns)
            unique_values = df[column].unique()
            selected_value = st.selectbox("Select value to filter by", unique_values)
            filtered_data = df[df[column] == selected_value]
            st.write(filtered_data)

        if st.checkbox("Show Data Plotting"):
            st.write("## Data Plotting")
            column = st.selectbox("Select column to plot", df.columns)
            plot_type = st.selectbox("Select plot type", ["Histogram", "Line", "Bar", "Scatter"])
            
            if plot_type == "Histogram":
                fig = px.histogram(df, x=column)
            elif plot_type == "Line":
                fig = px.line(df, x=df.index, y=column)
            elif plot_type == "Bar":
                fig = px.bar(df, x=df.index, y=column)
            else:
                y_column = st.selectbox("Select column for y-axis", df.columns)
                fig = px.scatter(df, x=column, y=y_column)

            st.plotly_chart(fig)

if __name__ == "__main__":
    main()
