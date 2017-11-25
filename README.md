# USB CAPDATA READER
Adli analizlerde veya ctf yarışmalarında sıklıkla karşılan pcap/pcapng analizleri yapılmaktadır. Bazen karşımıza usb dongle aracılığıyla alınan klavye verileri çıkmakta. Bunları "HUD Usage Table" üzerinden ascii formatına dönüştürmek mümkün. Fakat yüzlerce veri olduğunda bu işleri yapan bir araca ihtiyacınız oluyor. Yazdığım bu scriptin yaptığı şey de bu tam olarak.

1-) Tshark yardımıyla tüm capdata verilerini bir dosyaya alın (scriptin düzgün çalışması için bu dosyanın ismi "result.txt" olmalıdır).
    tshark -r sample.pcapng -T fields -e usb.capdata > result.txt

2-) Result.txt dosyasının içini açın ve üst tarafta eklenen fazladan boşlukları silin ve diğer veriler üzerinde değişiklik yapmadan kaydedin (keyboard.txt, result.txt ve usb_dongle.py aynı klasör içinde olmalıdır)

3-) Usb_dongle.py dosyasını çalıştırın ve seçenek kısmında 2 yi seçin. Otomatik olarak verileri alıp klavye karşılıklarını bularak ekrana yazdıracaktır.

