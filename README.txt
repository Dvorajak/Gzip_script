Script je vytvořen pro vytvoření gzip souborů ze složky /var/log/ a je vytvořen v Pythonu

Kód je napsán tak, že vytvoří gzip soubory s překopírovaným obsahem z .log souborů které následně smaže, tak se tedy zachovají pouze archivované soubory.
Při psaní kódu jsem vytvořil dočasnou složku se soubory .log abych otestoval funkčnost na systému Windows. Po úspěšném ověření funkčnosti jsem script otestoval na virtuálním linuxovém zařízení Linuxmin,
kde jsem script spustil příkazem 'python3 GyipLog.py' a ověřil zda opravdu konvertoval veškeré logy v námi požadované složce.

- po spuštění příkazu a spuštění scriptu 'python3 GyipLog.py' archivuje všechny soubory *.log na *.log.gz ve složce /var/log/
- lze tedy založit cronjob pomocí 'crontab -e' a následně '0 0 1 * * /usr/bin/python3 /root/GzipLog.py' kde udávám celou cestu jak ke scriptu tak k pythonu 
- Po uložení máme vytvořený cronjob který se spustí jednou za měsíc

Script je navržen na archivování logů kvůli zmenšení velikosti. Jednoduchou úpravou scriptu můžeme ovšem dosáhnout na archivaci v jiných složkách a jiných souborů.
Lze tak např. archivovat staré programy nebo již nepožívaný kód.
