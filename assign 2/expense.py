from datetime import datetime
class Expense:
    def __init__(self,expense_id,date,category,description,amount) -> None:
        self.expense_id = expense_id
        self.date = datetime.strptime(date,"%Y-%m-%d").date()
        self.category = category
        self.description = description
        self.amount = amount

    def __str__(self) -> str:
         return f"""
         Expense details:
         id : {self.expense_id}
         date : {self.date}
         category : {self.category}
         description : {self.description}
         amount : {self.amount}
         """
