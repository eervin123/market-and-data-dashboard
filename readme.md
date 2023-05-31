# Cryptocurrency Dashboard

This is a Python script that creates a cryptocurrency dashboard using Dash, a Python framework for building analytical web applications. The dashboard displays real-time price charts and percentage change of two cryptocurrencies, Bitcoin (BTC) and Ethereum (ETH).

## Dependencies
- Dash: The main framework used to create the web application.
- Dash Bootstrap Components: Provides Bootstrap-themed Dash components for styling the dashboard.
- Plotly Express: A high-level data visualization library that simplifies creating interactive charts.
- yfinance: A Python library to access historical market data from Yahoo Finance.

## Getting Started
To get started with the dashboard, follow these steps:

1. Install the required dependencies. You can install them using pip by running the following command:
   ```
   pip install dash dash_bootstrap_components plotly yfinance
   ```

2. Copy and paste the provided code into a Python script.

3. Run the script. You can do this by executing the script from the command line:
   ```
   python <script_name>.py
   ```

4. Open a web browser and navigate to `http://localhost:8050`. You should see the cryptocurrency dashboard.

## Dashboard Features
The cryptocurrency dashboard consists of the following components:

- **Price Display**: The dashboard displays the current price of Bitcoin (BTC) and Ethereum (ETH). The prices are updated in real-time.
- **Percentage Change**: The dashboard also shows the percentage change in price for both cryptocurrencies. The change is calculated based on the difference between the most recent closing price and the closing price from the start of the day.
- **Price Charts**: The dashboard includes line charts for BTC and ETH. The charts show the historical price data for the selected cryptocurrencies. You can hover over the charts to view specific price values for a given date.
- **Update Data Button**: There is a button labeled "Update Data" that can be clicked to manually update the data. Clicking this button triggers a callback that retrieves the latest price data for BTC and ETH and updates the charts and price display.

## Customization and Extension
If you want to customize or extend the dashboard, you can modify the provided code. Here are some possible modifications and additions you can make:

- **Adding Additional Cryptocurrencies**: You can add more cryptocurrencies by retrieving their price data using the `yfinance` library and creating additional figure objects for the charts.
- **Changing the Dashboard Layout**: You can modify the layout of the dashboard by editing the `layout` variable. You can add new components, change the styling, or rearrange the existing components.
- **Adding Additional Functionality**: You can add new features to the dashboard, such as additional charts, data analysis, or integration with external APIs. You can do this by extending the existing code and creating new callbacks.

## Development Tips
- When making changes to the code, you can save the file, and the Dash application will automatically reload with the updated changes.
- If you encounter any errors or issues, you can refer to the Dash documentation (https://dash.plotly.com/) or seek assistance from the Dash community.

## Next Steps
To continue working on the dashboard and add new features, you can follow these steps:

1. Share this README file with the intern to provide them with an overview of the dashboard and its current state.

2. Discuss the specific tasks or features that need to be completed.

3. Provide access to the necessary APIs, libraries, or resources required to complete the tasks.

4. Encourage the intern to explore the existing code, understand the Dash framework, and refer to the documentation or relevant examples.

5. Set up regular check-ins or code reviews to provide guidance and feedback on their progress.
