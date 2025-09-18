# API iki farklı yazılımın birlikte entegre çalışmasını sağlar.
# Bir e-ticaret sitesinde ödeme için farklı ödeme platformlarının kullanılması API e bir örnektir.

from fastapi import FastAPI # Öncelikle FastAPI sınıfını alıyoruz.
import random
from pydantic import BaseModel
from typing import Optional,Union


class Urun(BaseModel):
    isim: str
    fiyat: float                 # Bir şablon oluşturduk.
    stok: int
    kategori: Union[str,None] = None




app = FastAPI() # app olarak fastapi sınıfından bir nesne oluşturuyoruz.

@app.get("/")  # get ile ne döndüreceğimizi bir fonksiyon ile belirliyoruz.
def read_root():
    return {"output":"Umutsuz durumlar yoktur. Umutsuz insanlar vardır."}
    # Burada bize JSON çıktı veriyor.


@app.get("/soz/{kisi}")
def soz(kisi):
    sozler = {
        "ataturk": "Umutsuz durumlar yoktur, umutsuz insanlar vardır.",
        "mevlana": "Ne olursan ol yine gel.",
        "tesla": "çok çalısın abi."
    }
    if kisi == "rastgele":
        cikti = random.choice(list(sozler.values()))
    else:
        cikti = sozler.get(kisi.lower())

    return {"output": cikti}

# Pydantic Verileri gruplandırmayı sınıflandırmayı ve kontrol etmeyi sağlayan kütüphanedir.


@app.post("/urun/")
def urun(urun:Urun):
    urun_dict = urun.dict()
    urun.stok = max(0,urun.stok)
    urun_dict.update({"stoktavar": urun.stok > 0})
    return {"output": urun_dict}

