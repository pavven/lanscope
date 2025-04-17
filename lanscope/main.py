from core.scanner import network_scan

def menu():
    while True:
        print("\n=== LANSCOPE ===")
        print("1. Skanuj sieć lokalną")
        print("0. Wyjście")

        choice = input("Wybierz opcję: ")

        if choice == "1":
            subnet = input("Podaj podsieć (np. 192.168.1.0/24): ")
            network_scan(subnet)
        elif choice == "0":
            print("Zamykanie programu...")
            break
        else: 
            print("Nieprawidłowa opcja.")

if __name__ == "__main__":
    menu()

