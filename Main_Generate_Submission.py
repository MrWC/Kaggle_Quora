import pandas as pd
from datetime import datetime

result = pd.read_csv("./0508/submission_0.4463.csv")
result.shape

result.ix[result.is_duplicate >= 0.6, "is_duplicate"] = int(1)
result.ix[result.is_duplicate < 0.6, "is_duplicate"] = int(0)
result.is_duplicate = result.is_duplicate.astype(int)
result.to_csv("Submission"+datetime.now().strftime("%y-%m-%d_%H-%M"), index=False)