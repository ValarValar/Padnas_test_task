import os

import pandas as pd

FILE_NAME = "test_data.csv"
DATA_PATH = f"{os.getcwd()}\data\{FILE_NAME}"

# Чтобы не создавать датафрейм с тестовыми даными, решил использовать готовый
# для наглядности брал разницу в 2 дня, так как в тестовом датасете разницы в 3 минуты нет
SESSION_TIME_DELTA = pd.Timedelta(days=2)

data_df = pd.read_csv(DATA_PATH)
data_df = data_df.sort_values(by=['customer_id', 'timestamp'])
data_df['timestamp'] = data_df['timestamp'].apply(lambda x: pd.to_datetime(x, unit='s'))

gt_3min = data_df['timestamp'].diff().abs() > SESSION_TIME_DELTA
diff_user = data_df['customer_id'].diff().abs() > 0

session_id = (diff_user | gt_3min).cumsum()
data_df['session_id'] = session_id
