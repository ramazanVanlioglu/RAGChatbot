
"""Yanıtın üretilmesi -> Dil modeli kullanımı."""
#from transformers import pipeline

#generative pre-trained transformer gibi bir dil modeli yükleme
generator=pipeline("text-generation",model='gorkemgoknar/gpt2-small-turkish')
def generate_response(query,results):
  context = "\n".join(
        [f"{res['Ders Adı']}, {res['Açıklama']} (Tarih: {res['Sınav Tarihi']}) (Öğretmen: {res['Öğretmen']})" for res in results]
    )

  prompt = f"""
  Soruya aşağıdaki bilgileri kullanarak kısa ve net bir cevap ver:

  Bilgiler:
  {context}

  Soru:
  {query}

  Cevap:
  """

  response = generator(prompt, max_length=150, num_return_sequences=1, top_k=50, top_p=0.95, do_sample=True,truncation=True)

  return response[0]['generated_text']# --> pipeline için

response=generate_response(query,results)
print("Yanıt:",response)