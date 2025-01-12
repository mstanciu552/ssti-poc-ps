# Calculator Simplu - Documentație

Această aplicație este un calculator simplu, bazat pe un frontend scris în HTML și un backend în Flask. Scopul aplicației este de a efectua operații de adunare între două numere introduse de utilizator, cu posibilitatea de a explora și testa vulnerabilitățile de tip Server-Side Template Injection (SSTI).

---

## Cum funcționează aplicația

### 1. Frontend (HTML + JavaScript):
- **Interfața** permite utilizatorului să introducă două numere într-un formular simplu.
- După apăsarea butonului **Adună numerele**, valorile sunt trimise către server folosind un request HTTP POST, sub formă de JSON.
- Rezultatul calculului este afișat pe pagină sau, în cazul unei erori, un mesaj corespunzător.

### 2. Backend (Flask):
- Serverul Flask preia valorile trimise de frontend și le procesează.
- Calculul este realizat fie într-un mod sigur, fie intenționat vulnerabil (pentru testarea SSTI).
- Rezultatul este returnat către frontend.

---

## Testarea vulnerabilităților SSTI

### Ce este SSTI?
SSTI (Server-Side Template Injection) este o vulnerabilitate care apare atunci când input-urile utilizatorului sunt interpretate și evaluate direct într-un motor de șabloane. Acest comportament poate permite unui atacator să execute cod arbitrar pe server.

### Cum se testează:
1. Introduce expresii precum `7 * 7` în câmpurile de input pentru a verifica dacă acestea sunt evaluate.
2. Încearcă expresii periculoase, cum ar fi:
   - `().__class__.__base__.__subclasses__()`
   - `config.__class__`  

Aceste expresii pot expune detalii sensibile despre server dacă acesta este vulnerabil.

---

## Prevenirea vulnerabilităților
Pentru a proteja aplicația:
- **Nu utiliza `render_template_string`** cu input nesecurizat.
- Validează și sanitizează toate datele introduse de utilizatori.
- Folosește instrumente de testare a securității aplicațiilor.


