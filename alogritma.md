class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def check_balance(self):
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Yetersiz bakiye. İşlem gerçekleştirilemedi."
        else:
            self.balance -= amount
            return f"İşlem başarılı! Yeni bakiyeniz: {self.balance} TL"

# Örnek hesap oluşturma
my_account = BankAccount("12345678", 5000)

# Kullanıcıdan çekmek istediği tutarı al
withdraw_amount = float(input("Çekmek istediğiniz tutarı girin:1100tl "))

# Para çekme işlemini yap
result = my_account.withdraw(withdraw_amount)

# İşlem sonucunu göster
print(result)
