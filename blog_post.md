# Can Ancient Geography Predict Roman Stamp Types? A Machine Learning Experiment

*Exploring 24,000 archaeological records with Random Forest and geographic coordinates*

---

When archaeologists dig up a Roman amphora — one of those ancient clay jars that carried olive oil, wine, or fish sauce across the empire — they sometimes find a small stamp pressed into the clay. That stamp tells us where the jar was made, who made it, and what it carried.

Over decades of fieldwork, researchers have recorded more than **24,000 of these stamp finds** across the former Roman Empire — from Britannia in the north to Mauretania Tingitana in North Africa. Each record tells us the type of stamp and the exact location where it was found.

That raises an interesting question: **can we predict the stamp type just by knowing where it was discovered?**

---

## The Questions I Set Out to Answer

Before building any model, I identified the key questions I wanted this data to answer:

1. **Which Roman provinces have the most recorded stamp finds?**
2. **What are the most common amphora types?**
3. **Can latitude and longitude alone predict the stamp type?**
4. **Which geographic axis — north/south or east/west — carries more predictive power?**

---

## What the Data Looks Like

The dataset comes from **CEIPAC** (Centre for the Study of Roman Amphoras) and contains 24,092 records across 9 columns, including coordinates, stamp type, province name, and archaeological site.

After cleaning — removing rows with missing province or type values, and filtering out stamp types with fewer than 100 records — I was left with **22,511 clean records** covering **17 stamp types**.

---

## Finding 1: Italia Dominated, But Trade Went Everywhere

The first thing that stands out is how unevenly stamps are distributed across provinces.

**Top 5 Provinces:**

| Province | Stamps Found |
|---|---|
| Italia | 6,832 |
| Narbonensis (southern France) | 3,498 |
| Tarraconensis (northeastern Spain) | 2,526 |
| Germania Superior | 2,365 |
| Britannia | 1,980 |

Italia leads — unsurprisingly, as it was both a major producer and consumer. But the strong presence in Britannia and the Germanic provinces tells a story of how far Roman trade networks stretched. A jar stamped in Baetica (modern Andalusia, Spain) could end up excavated near Hadrian's Wall two thousand years later.

---

## Finding 2: Dressel 20 Is Everywhere

When you look at stamp types, one name dominates: **Dressel 20**, with over **10,238 records** — more than double the second most common type (Brindisian amphora at 4,385).

Dressel 20 amphorae carried **Baetican olive oil**, one of the most traded commodities in the Roman world. Their wide distribution reflects the scale of the Roman olive oil trade, which was essentially an ancient version of a global supply chain.

---

## Finding 3: Geography Predicts Stamp Type Better Than Expected

Here's where it gets interesting from a machine learning perspective.

Using only two features — **latitude and longitude** — I trained two models:

| Model | Accuracy |
|---|---|
| **Random Forest** | **69.6%** |
| Logistic Regression | 62.5% |

The Random Forest model, validated with 5-fold cross-validation, achieved a mean accuracy of **71.8%**.

To be clear: predicting which of 17 stamp types was found at a location, using only coordinates, with nearly 70% accuracy — that is a meaningful result. It tells us that stamp types are **not randomly distributed across the landscape**. Different amphora types cluster in different geographic zones, which reflects the underlying structure of Roman trade routes and production regions.

Some types were extremely easy to predict:

- **Brindisian amphora**: 97% precision — because these were produced almost exclusively in southern Italy (Brindisi) and their distribution is tightly clustered
- **Dressel 20**: 96% precision — the dominant Spanish oil amphora, strongly associated with western provinces
- **Lamboglia 2**: 81% precision — concentrated in the Adriatic region

Other types were harder — particularly smaller, more regionally mixed types like Dressel 2-4 and Gauloise 4, which overlapped geographically with other types.

---

## Finding 4: Longitude Edges Out Latitude (Barely)

One of the cleaner insights from the feature importance analysis:

| Feature | Importance Score |
|---|---|
| Longitude (east-west position) | 51.7% |
| Latitude (north-south position) | 48.3% |

Both features contribute almost equally — which makes sense. The Roman Empire stretched both east-west (Britannia to Syria) and north-south (Germania to North Africa), and different amphora types were produced in different corners of that geography.

The slight edge to longitude may reflect the fact that major production zones — Spanish oil, Italian wine, Adriatic fish sauce — are more cleanly separated on an east-west axis than a north-south one.

---

## What This Means

A 70% accuracy from just two numbers — latitude and longitude — is genuinely surprising. It validates something historians already suspected: that **Roman trade was structured and regional**, not chaotic. Different goods traveled well-worn routes, and those routes left a detectable geographic fingerprint in the archaeological record.

Machine learning didn't discover this pattern — archaeologists already knew it. But it quantified it, and confirmed that the pattern is strong enough to be statistically predictive.

---

## Limitations and What Could Be Improved

This model has real limitations worth acknowledging:

- **Imbalanced classes**: Dressel 20 makes up nearly half the dataset. The model is naturally biased toward predicting it.
- **Only two features**: Adding province name, site type, or temporal data would likely improve accuracy significantly.
- **No temporal dimension**: The dataset spans several centuries of Roman history. Stamp patterns likely shifted over time.

A more sophisticated model incorporating text features (site names, stamp codes) and time period could push accuracy considerably higher.

---

## Conclusion

Starting with a dataset of ancient clay stamps and two coordinate columns, a Random Forest classifier reached **~70% accuracy** in predicting the amphora type. The model works because Roman trade was geographically structured — and that structure persists in the archaeological record.

Geography alone carries real signal. And sometimes, that is enough.

---

*Dataset: CEIPAC — Centre for the Study of Roman Amphoras*  
*Tools: Python, pandas, scikit-learn, matplotlib, seaborn*  
*Author: Abdulrahman — Udacity Data Science Nanodegree*
