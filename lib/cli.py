def main():
    from main import  fetch_cities, get_city, update_city, delete_city, get_forecast_by_city
    from main import fetch_forecasts,  delete_forecast
    

    while True:
        print("\n📡 TERMOCAST CLI")
        print("1. Manage Locations")
        print("2. Manage Forecasts")
        print("3. Manage Weather Records")
        print("0. Exit")
        main_choice = input("Enter your choice: ")

        if main_choice == "1":
            print("\n📍 LOCATION MENU")
            
            print("1. List Locations")
            print("2. View Location by ID")
            print("3. Update Location")
            print("4. Delete Location")
            
            print("0. Exit")

            choice = input("Enter your choice: ")
            if choice == "1":
                fetch_cities()
            elif choice == "2":
                get_city()
            elif choice == "3":
                update_city()
            elif choice == "4":
                delete_city()
            
            elif choice == "0":
                break
            else:
                print("❌ Invalid input! Try again.")

        elif main_choice == "2":
            print("\n🌤 FORECAST MENU")
            
            print("1. List All Forecasts")
            print("2. View Forecast by ID")
            print("3. Update Forecast")
            
            print("0. Exit")

            choice = input("Enter your choice: ")
            if choice == "1":
                fetch_forecasts()
            elif choice == "2":
                get_forecast_by_city()
            
            elif choice == "3":
                delete_forecast()
            elif choice == "0":
                break
            else:
                print("❌ Invalid input! Try again.")

        
          



        elif main_choice == "0":
            print("Goodbye from TermoCast! 👋")
            break

        else:
            print("❌ Invalid input! Try again.")

if __name__ == "__main__":
    main()