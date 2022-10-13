class Farm:
    
    # Qiymətlər bu şəkildədir: yumurta - 50, yun - 125, sut - 200.
    
    __wool_price = 125
    __egg_price = 50
    __milk_price = 200
    __cows_price = 800
    __chickens_price = 200
    __sheeps_price = 500
        
    
    # Yaranan object başlanğıc dəyər kimi özünə enkapsulyasiya olunmuş pul və yem_sayi dəyərləri alsın. pul 0, yem_sayi isə 15 olsun.
      
    def __init__(self, *args):
        self.__money = 0
        self.__feed_amount = 15
        self.animals = [*args]     
        
    @property
    def chickens_count(self):
        return self.animals.count('toyuq')
    
      
        
    @property
    def cows_count(self):
        return self.animals.count('inek')
    
        
        
    @property
    def sheeps_count(self):
        return self.animals.count('qoyun')
    
    
    @property
    def cows_price(self):
        return self.__cows_price

    @property
    def chickens_price(self):
        return self.__chickens_price
    
    @property
    def sheeps_price(self):
        return self.__sheeps_price
    
          
        
    # pul miqdarını getter ilə yazın ki, sadəcə görmək mümkün olsun, dəyişdirmək olmasın. 
    
    @property
    def money(self):
        return self.__money
    
    
    # yem_sayi atributu yem_sayı adlı getter (@property) edilmiş metod ilə göstərilsin. yem_sayi dəyəri vermək üçün də bir setter qurun. 
    # Əgər bərabər edilən yem mövcud yem sayından kiçikdirsə hər yemə görə 15 pul əlavə edin, əgər mövcud saydan çoxdursa hər yemə görə 25 pul çıxın. 
    
    @property
    def feed_amount(self):
        return self.__feed_amount
    
    
    # Yem bərabərləşdirilərkən qeyd edilən yem sayı mənfi dəyərdirsə və ya mövcud pulla alına bilməyəcək qədər çoxdursa ValueError verin.
    
    @feed_amount.setter
    def feed_amount(self, new_value):
        if new_value < self.__feed_amount:
            self.__money += (self.__feed_amount - new_value) * 15
        elif new_value > self.__feed_amount:
            self.__money -= (new_value - self.__feed_amount) * 25
            if self.__money < 0:
                raise WalletError("you don't have enough money")
        else:
            self.feed_amount = new_value
            
    
    
    # sut_sat, yumurta_sat, yun_sat metodları olsun. Misal üçün əgər yumurta_sat funksiyası işə düşərsə 
    # fermada olan toyuq sayı qədər yem_sayından çıxılsın və əldə edilən yumurtanın sayının qiymətinə hasili 
    # qədər qazanc əldə olunaraq pul dəyərinə əlavə edilsin. Qiymətlər bu şəkildədir: yumurta - 50, yun - 125, sut - 200.
    
    def sud_sat(self):
        self.__money += (self.feed_amount - self.cows_count) * self.__milk_price
    
    def yun_sat(self):
        self.__money += (self.feed_amount - self.sheeps_count) * self.__wool_price
    
    def yumurta_sat(self):
        self.__money += (self.feed_amount - self.chickens_count) * self.__egg_price 
        
    
    
    # Classda list və ya tuple şəklində girilən heyvanların qiymətlərini
    # hesablayıb return edən bir static method hazırlayın. Qiymətlər bu şəkildə olacaq: İnek: 800, qoyun: 500, toyuq: 200.
    
    
    
    
    
    # heyvanlar_al deyə bir metod olsun və tuple və ya list tipində heyvanların olduğu elementlərdən ibarət data qəbul etsin. 
    # Alınması istənilən heyvanların qiymətini bundan əvvəl yaratdığınız static method ilə əldə edin. Əgər həmin qiymətdən az pul varsa 
    # ValueError verin əgər kifayət qədər pul varsa həmin puldan çıxıb, heyvanları digər heyvanların yanına qatın
    
    
animals = ['inek','inek','qoyun','inek','qoyun']
    
    
ferma = Farm('inek', 'inek', 'toyuq', 'inek', 'qoyun', 'qoyun', 'toyuq', 'qoyun')



# print(ferma.feed_amount)

print(ferma.get_animals_prices(animals))

# ferma.sud_sat()
# print(ferma.feed_amount)

# print(ferma.chicken_count())
# print(ferma.animals)


# print(ferma.animals)




