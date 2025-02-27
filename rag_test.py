import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
from transformers import pipeline
#ctrl-alt-down -->> select multiple lines

#!csv'den veriyi yükleme

data=pd.read_csv("augmented_questions.csv")
data.head();

#?vektörlerin oluşturulması ve indeksleme
#paraphrase-multilingual-MiniLM-L12-v2
#all-MiniLM-L6-v2
#model yükleme
model=SentenceTransformer("all-MiniLM-L6-v2")

#veriyi hazırlama
corpus=data.apply(lambda row:f"row{'soru'} - {row['cevap']}", axis=1).tolist()

#vektörleri oluşturma
corpus_embeddings=model.encode(corpus)

#faiss indeks oluşturma
index=faiss.IndexFlatL2(corpus_embeddings.shape[1])
index.add(corpus_embeddings)

print(f"İndekslenen kayıt sayısı: {index.ntotal}")

#*sorgu işleme -> kullanıcıdan gelen soruyu vektörleştirelim
#ve en yakın sonuçları faiss
#ile bulalım.

def search(query,k=1):
    query_vector=model.encode([query])
    distances,indices=index.search(query_vector,k)
    results=[]
    for idx in indices[0]:
        results.append(data.iloc[idx].to_dict())
    return results

## örnek sorgu
"""cevap=""
while cevap!='h':
    query=input("Bir soru sorun:")
    results=search(query)
    for result in results:
        print(f"Cevap: {result['cevap']}")
    cevap=input("Devam mı?(e/h):")
    print("\n\n")"""