import os

import pandas as pd

FILE_NAME = "test_data.csv"
DATA_PATH = f"{os.getcwd()}\data\{FILE_NAME}"

# Чтобы не создавать датафрейм с тестовыми даными, решил использовать готовый.
# Для наглядности брал разницу в 1 день, так как в тестовом датасете разницы в 3 минуты нет
SESSION_TIME_DELTA = pd.Timedelta(days=1)

data_df = pd.read_csv(DATA_PATH)
data_df = data_df.sort_values(by=['customer_id', 'timestamp'])
data_df['timestamp'] = data_df['timestamp'].apply(lambda x: pd.to_datetime(x, unit='s'))

gt_3min = data_df['timestamp'].diff() > SESSION_TIME_DELTA
diff_user = data_df['customer_id'].diff() > 0

session_id = (diff_user | gt_3min).cumsum()
data_df['session_id'] = session_id
