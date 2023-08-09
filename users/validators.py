import os

import pandas as pd
from django.core.exceptions import ValidationError


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.xlsx']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


def validate_file_data(file):
    user_data = pd.read_excel(file['file'], engine='openpyxl')
    csv_columns = list(user_data.columns)
    error_list = []
    if 'expense' in csv_columns:
        if not all(isinstance(x, int) for x in user_data['expense']):
            error_list.append("Expense column can only contain numeric values.")
    else:
        error_list.append("Expense column missing in uploaded file.")
    if 'category' in csv_columns:
        category_data = user_data.get('category', []).dropna()
        expense_data = user_data.get('expense', []).dropna()
        if not len(category_data) == len(expense_data):
            error_list.append("Category or Expense column contains some missing values.")
    else:
        error_list.append("Category column missing in uploaded file.")
    return error_list
