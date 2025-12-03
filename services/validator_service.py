from datetime import datetime, date, timedelta


class Validator:
    minimum_name_length = 2 # Shortest name I know is Bo or My. Maybe you know a shorter name?
    @staticmethod
    def is_valid_first_name(first_name: str) -> bool:
        # This is a start. Add more rules.
        if len(first_name) < Validator.minimum_name_length:
            return False
        
        return True
    
    ## You can also make the validator more dynamic like this
    # @staticmethod
    # def is_valid_first_name(first_name: str, minimum_length: int = 2) -> bool:
    #     # This is a start. Add more rules.
    #     if len(first_name) < minimum_length:
    #         return False
        
    #     return True

    @staticmethod
    def is_valid_last_name(last_name: str) -> bool:
        return False

    @staticmethod
    def is_valid_email(email: str) -> bool:
        return False

    @staticmethod
    def validate_dates(start_date: str, end_date: str) -> bool:
        # This converts a string to a date using YYYY-MM-DD as format
        date_obj = datetime.strptime(start_date, "%Y-%m-%d").date()

        # Use this to find out today's date
        today = date.today()

        # One day in the future
        tomorrow = today + timedelta(days=1)
        return False
