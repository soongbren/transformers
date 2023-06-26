### Menterjemah dokumentasi Transformers ke dalam bahasa anda

Sebagai sebahagian daripada misi kami untuk mendemokrasikan pembelajaran mesin, kami ingin menjadikan perpustakaan Transformers tersedia dalam lebih banyak bahasa! Ikuti langkah di bawah jika anda ingin membantu menterjemah dokumentasi ke dalam bahasa anda 🙏.

**🗞️ Buka isu**

Untuk bermula, navigasi ke halaman [Isu](https://github.com/huggingface/transformers/issues) repo ini dan semak sama ada orang lain telah membuka isu untuk bahasa anda. Jika tidak, buka isu baharu dengan memilih "Templat terjemahan" daripada butang "Isu baharu".

Setelah isu wujud, siarkan ulasan untuk menunjukkan bab yang anda ingin kerjakan dan kami akan menambahkan nama anda pada senarai.


**🍴 Garpu repositori**

Mula-mula, anda perlu [membuat repo Transformers](https://docs.github.com/en/get-started/quickstart/fork-a-repo). Anda boleh melakukan ini dengan mengklik pada butang **Fork** di penjuru kanan sebelah atas halaman repo ini.

Sebaik sahaja anda membuat repo, anda perlu mendapatkan fail pada mesin tempatan anda untuk diedit. Anda boleh melakukannya dengan mengklon garpu dengan Git seperti berikut:

```bash
git clone https://github.com/YOUR-USERNAME/transformers.git
```

**📋 Salin-tampal versi Inggeris dengan kod bahasa baharu**

Fail dokumentasi berada dalam satu direktori utama:

- [`docs/source`](https://github.com/huggingface/transformers/tree/main/docs/source): Semua bahan dokumentasi disusun di sini mengikut bahasa.

Anda hanya perlu menyalin fail dalam direktori [`docs/source/en`](https://github.com/huggingface/transformers/tree/main/docs/source/en), jadi navigasi ke anda terlebih dahulu garpu repo dan jalankan yang berikut:

```bash
cd ~/path/to/transformers/docs
cp -r source/en source/LANG-ID
```

Di sini, `LANG-ID` mestilah salah satu daripada kod bahasa ISO 639-1 atau ISO 639-2 -- lihat [di sini](https://www.loc.gov/standards/iso639-2/php/code_list. php) untuk jadual yang berguna.

**✍️ Mula menterjemah**

Bahagian yang menyeronokkan datang - menterjemah teks!

Perkara pertama yang kami cadangkan ialah menterjemah bahagian fail `_toctree.yml` yang sepadan dengan bab dokumen anda. Fail ini digunakan untuk memaparkan jadual kandungan di laman web.

> 🙋 Jika fail `_toctree.yml` belum wujud untuk bahasa anda, anda boleh menciptanya dengan menyalin-tampal daripada versi Inggeris dan memadamkan bahagian yang tidak berkaitan dengan bab anda. Cuma pastikan ia wujud dalam direktori `docs/source/LANG-ID/`!

Medan yang perlu anda tambah ialah `tempatan` (dengan nama fail yang mengandungi terjemahan; cth. `autoclass_tutorial`), dan `title` (dengan tajuk dokumen dalam bahasa anda; cth. `Muatkan contoh terlatih dengan AutoClass` ) -- sebagai rujukan, berikut ialah `_toctree.yml` untuk [Bahasa Inggeris](https://github.com/huggingface/transformers/blob/main/docs/source/en/_toctree.yml):

```yaml
- sections:
  - local: pipeline_tutorial # Do not change this! Use the same name for your .md file
    title: Pipelines for inference # Translate this!
    ...
  title: Tutorials # Translate this!
```

Setelah anda menterjemah fail `_toctree.yml`, anda boleh mula menterjemah fail [MDX](https://mdxjs.com/) yang dikaitkan dengan bab dokumen anda.

> 🙋 Jika anda ingin orang lain membantu anda dengan terjemahan, anda harus [membuka isu](https://github.com/huggingface/transformers/issues) dan menandai @sgugger.
