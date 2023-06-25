from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton,
 QPushButton, QLabel,QButtonGroup)


#hafta3/ hafta4
from random import shuffle,randint #liste içerisindeki elemanların karıştırılmasını sağlar.


#Soru sınıfını oluşturalım.
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


questions_list = [] 
questions_list.append(Question('Brezilya\'nın resmi dili', 'Portekizce', 'ingilizce', 'İspanyolca', 'Brezilyaca'))
questions_list.append(Question('Rusya bayrağında hangi renk yoktur?', 'Yeşil', 'Kırmızı', 'Beyaz', 'Mavi'))
questions_list.append(Question('Yakutların yöresel evleri', 'Urasa', 'Yurt', 'İglo', 'Peri bacaları'))
questions_list.append(Question("Türklerin ilk kullandığı alfabe hangisidir?","Göktürk Alfabesi","Uygur Alfabesi","Arap Alfabesi", "Çin Alfabesi"))
questions_list.append(Question("Demokrasiyi ilk hangi ülke bulmuştur?","Yunanistan","İngiltere","Türkiye","Almanya"))
questions_list.append(Question("Türkiye'nin yüz ölçümü ne kadar","783.256 kilometrekare","5.200.000 kilometrekare","86.600 kilometrekare","881.000 kilometrekare"))

#--
app = QApplication([])
 
window = QWidget()
window.setWindowTitle('Memo Card')
window.resize(400,400)
 
'''Memory Card uygulamasının arayüzü'''
btn_OK = QPushButton('Cevapla') # cevap düğmesi
lb_Question = QLabel('Moskova hangi yılda kuruldu?') # soru metni
 
RadioGroupBox = QGroupBox("Cevap seçenekleri") # ekrandaki grup cevapları olan anahtarlar içindir
rbtn_1 = QRadioButton('1147')
rbtn_2 = QRadioButton('1242')
rbtn_3 = QRadioButton('1861')
rbtn_4 = QRadioButton('1943')


#2.hafta
#buton grubun oluşturulması
RadioGroup=QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
#--


layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() # dikey olanlar yatay olanın içinde olacak
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) # ilk sütuna iki cevap
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # ikinci sütuna iki cevap
layout_ans3.addWidget(rbtn_4)
 
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) # sütunlar tek satıra yerleştirildi
 
RadioGroupBox.setLayout(layout_ans1) # cevap seçeneklerini içeren "panel" hazır 


#2.hafta
#test sonucunun doğruluğunun tespiti
#Sonuç paneli
AnsGroupBox=QGroupBox("Test sonucu")
lb_Result=QLabel('Doğru mu yanlış mı')
lb_Correct=QLabel('Cevap burada olacak')


layout_res=QVBoxLayout()
layout_res.addWidget(lb_Result,alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct,alignment=Qt.AlignHCenter,stretch=2)
AnsGroupBox.setLayout(layout_res)
#--


layout_line1 = QHBoxLayout() # soru
layout_line2 = QHBoxLayout() # cevap seçenekleri veya test sonucu
layout_line3 = QHBoxLayout() # "Cevapla" düğmesi
 
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
# Her iki paneli de aynı çizgiye yerleştiriyoruz, biri gizlenecek, diğeri gösterilecek:
#hafta2
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()
#--


layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # düğme büyük olmalı
layout_line3.addStretch(1)
 
# Şimdi oluşturulan satırları birbirinin altına yerleştireceğiz:
layout_card = QVBoxLayout()
 
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # içerik arasındaki boşluklar


#2.hafta
def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Sıradaki soru')


def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Cevapla')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)


#3.hafta
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]


def ask(q: Question):
    ''' fonksiyon, soru ve cevapların değerlerini ilgili widgetlara yazar, 
    cevap seçenekleri ise rastgele dağıtılır '''
    shuffle(answers) # düğme listesi karıştırıldı, artık listenin ilk sırasında öngörülemeyen bir düğme var
    answers[0].setText(q.right_answer) # listenin ilk öğesini doğru cevapla dolduralım, geriye kalanlar yanlış cevaplarla doldurulacak
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question) # soru
    lb_Correct.setText(q.right_answer) # cevap 
    show_question() # soru panelini gösteriyoruz 


def show_correct(res):
    ''' sonucu gösterme - iletilen metni "sonuç" etiketine yerleştirelim ve gerekli paneli gösterelim '''
    lb_Result.setText(res)
    show_result()


def check_answer():
    ''' eğer herhangi bir cevap seçeneği seçili ise kontrol edilip cevap panelinin gösterilmesi gerekmektedir'''
    if answers[0].isChecked():
        # doğru cevap!
        show_correct('Doğru!')
        #4.hafta
        window.score += 1
        print('İstatistik\n-Toplam soru: ', window.total, '\n-Doğru cevap: ', window.score)
        print('Puanlama: ', (window.score/window.total*100), '%')
        #--
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            # yanlış cevap!
            show_correct('Yanlış!')
            print('Puanlama: ', (window.score/window.total*100), '%')#4.hafta


def next_question():
    #4.hafta
    ''' listeden sıradaki soruyu soruyor '''
    window.total += 1
    print('İstatistik\n-Toplam soru: ', window.total, '\n-Doğru cevap: ', window.score)
    cur_question = randint(0, len(questions_list) - 1)  # eski değere ihtiyaçımız yoktur,                                                  # bu nedenle lokal bir değişken kullanılabilir! 
    # rastgele listeden bir soru alındı
    # yaklaşık yüz kelime girilirse, nadiren tekrarlanır
    q = questions_list[cur_question] # soruyu aldık
    ask(q) # soruldu
    #--


def click_OK():
    ''' başka sorunun gösterilip gösterilmeyeceğini veya bu soruya verilen cevabın kontrol edilip edilmeyeceğini belirler'''
    if btn_OK.text() == 'Cevapla':
        check_answer() # cevabın kontrolü
    else:
        next_question() # sıradaki soru
#--



window.setLayout(layout_card)


'''
Sil 4.hafta
window.cur_question=-1 #3.hafta


'''
#4.hafta
window.score = 0#doğru cevapların sayası
window.total = 0#kaç soru soruldu
#--
next_question() #3.hafta
btn_OK.clicked.connect(click_OK) #3.hafta
window.show()
app.exec()



