
# Analisi traffico — script statistico

Questo progetto contiene uno script Python per l'analisi esplorativa di due colonne di traffico presenti nel file CSV `traffico16.csv` (es. `ago1` e `ago2`). Lo script calcola statistiche di base, individua outlier con due metodi e verifica la normalità della distribuzione.

**Caratteristiche principali**
- **Statistiche**: media, deviazione standard, mediana, IQR.
- **Rilevamento outlier**: metodo basato su deviazione standard e metodo IQR.
- **Test di normalità**: test di Shapiro per decidere il metodo di rilevamento outlier.
- **Visualizzazione**: boxplot comparativo per le colonne analizzate.

**Requisiti**
- Python 3.8+
- numpy
- pandas
- matplotlib
- scipy

Installazione rapida delle dipendenze:

```bash
pip install numpy pandas matplotlib scipy
```

**Uso**
1. Posiziona `traffico16.csv` nella stessa cartella del progetto.
2. Apri (se necessario) `main.py` e modifica le variabili `month1` e `month2` per scegliere le colonne da analizzare.
3. Esegui lo script:

```bash
python main.py
```

Lo script stamperà a terminale le statistiche calcolate, gli outlier identificati per ciascun metodo e mostrerà un boxplot interattivo.

**File nel progetto**
- [main.py](main.py): script principale che esegue l'analisi.
- [traffico16.csv](traffico16.csv): dataset di esempio (non incluso automaticamente).
- [README.md](README.md): questo file.

**Note**
- Il test di Shapiro richiede campioni non troppo grandi per essere affidabile; per dataset molto grandi valutare test alternativi o un campionamento.
- I criteri per outlier usati nello script (1.5 * std e 1.5 * IQR) possono essere adattati secondo necessità.

