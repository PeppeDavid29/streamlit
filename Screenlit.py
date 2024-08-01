{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "c3ad61c7-1e9e-4b72-8b9b-5f59878dd150",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-08-01 21:35:01.803 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\sharo\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import psycopg2\n",
    "import pandas as pd\n",
    "\n",
    "# Database connection parameters\n",
    "DB_NAME = 'postgre_weather_data'\n",
    "DB_USER = 'postgres'\n",
    "DB_PASSWORD = 'shah123'\n",
    "DB_HOST = 'localhost'\n",
    "DB_PORT = '5432'\n",
    "\n",
    "# Function to fetch data from PostgreSQL\n",
    "def fetch_data():\n",
    "    conn = None\n",
    "    data = None\n",
    "    try:\n",
    "        # Connect to the PostgreSQL database\n",
    "        conn = psycopg2.connect(\n",
    "            host=DB_HOST,\n",
    "            port=DB_PORT,\n",
    "            dbname=DB_NAME,\n",
    "            user=DB_USER,\n",
    "            password=DB_PASSWORD\n",
    "        )\n",
    "\n",
    "        # Create a cursor object\n",
    "        cur = conn.cursor()\n",
    "\n",
    "        # Execute a query\n",
    "        cur.execute(\"SELECT * FROM ordered_by_city\")  # Replace with your query\n",
    "\n",
    "        # Fetch all rows from the executed query\n",
    "        rows = cur.fetchall()\n",
    "\n",
    "        # Get column names\n",
    "        colnames = [desc[0] for desc in cur.description]\n",
    "\n",
    "        # Create a DataFrame\n",
    "        data = pd.DataFrame(rows, columns=colnames)\n",
    "\n",
    "        # Close the cursor and connection\n",
    "        cur.close()\n",
    "    except (Exception, psycopg2.DatabaseError) as error:\n",
    "        st.error(f\"Error: {error}\")\n",
    "    finally:\n",
    "        if conn is not None:\n",
    "            conn.close()\n",
    "    return data\n",
    "\n",
    "# Streamlit app\n",
    "st.title(\"PostgreSQL Data Display\")\n",
    "\n",
    "# Fetch data from PostgreSQL\n",
    "data = fetch_data()\n",
    "\n",
    "# Display data in Streamlit\n",
    "if data is not None:\n",
    "    st.dataframe(data)\n",
    "else:\n",
    "    st.write(\"No data to display.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "8f8c4608-4594-40a6-82d3-6e151d2b0054",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

