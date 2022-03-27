<p align="center"><a href="https://github.com/MansaGroup/kanedama" target="blank"><img src="../.github/assets/logo.png" width="80" alt="Mansa's Logo" /></a></p>
<h1 align="center">Mansa's data science technical test</h1>
<p align="center">El Mahdi L'KOTBI</b> 💜</p>

# Introduction

The aim of this technical test is to first build a machine learning model that is able to predict next month outgoing given the past 6 months of transactions of a given account, and then deploy it using FastAPI.

# Usage
- Run 'make server' in order to run the server as a standalone
- Run 'make test' in order to run the test script (the server needs to be on)
- Run 'make compose' in order to run docker-composer pipeline (run server container -> run test container)

# Mythology
## Data science part

Here is the data processing pipeline that i've applied to the original data (transactions.csv, account.csv) : 
illust1

I have based my analysis on this hypothesis : 1 month is a 30 days period.
 
### Improvements
- Research on the best approachs to forecast an account's outgoings (feature ideas, model types, ensembling...)
- Create more features in order to capture insights about the accounts having more than 6 months of history (avg/std balance/outgoing...)
- Research on the best approachs to handle sparse timeseries


## Data engineering part
Here are the changes I applied to the original repository's architecture : 
- Separating python scripts into src/test, adding a folder for binary files
- Transforming the code logic to be OOP friendly
- Adding tests with real data extracted from the original data
- Dockerizing the server component and the test component
- Adding a makefile to make life easier

### Improvements
- Adding more automation/monitoring to the RegressionModel class (training a new model, validation, params/metrics logging...)
- Using a better format for saving the model (PMML, ONNX...)
- Adding throughput analysis script in order to evaluate the server's capacity
