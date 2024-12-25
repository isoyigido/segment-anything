Not: results/liver/point, results_txt, scores/v1_rerun, scores/v1_rerun/sam_prompt_binary_names_liver.json, sa_liver/images, sa_liver/masks klasör ve dosya adları böyle olmak zorunda. sa_liver içerisinde images ve masks içerisindeki resimler ve maskeleri aynı ada sahip olmalı. (örneğin images/abc.png ve masks/abc.png eşleşir)

segment_anything içerisinde asıl yapay zekâ modeli var. (predictor.py içerisinde SamPredictor())

scripts dosyasında bir şeylerin kodu var.

ritm_interactive_segmentation aslında opsiyonel, makaleyi yazan kişilerin kullandığı bir şey.

sa_liver içerisinde veri setimiz var. (images içerisinde resimler, masks içerisinde maskeler)

sam_vit_h_4b8939.pth internetten indirilen önceden train edilmiş genel amaçlı model (2,39 GB)
coco_lvis_h32_itermask.pth ritm_interactive_segmentation'ın çalışması için gerekli.

prompt_gen_and_exec_v1.py makaleyi yazan kişilerin kodu (asıl çalıştırılan kod)
prompt_gen_and_exec_v2_allmode.py şimdilik kullanmadım, çalışmıyor olabilir.

Bu dosya içerisinde:
vis=True ise sonuçlar results/liver/point içerisine kaydediliyor. (gt, input, pred, prompt)
vis=False ise sonuçlar scores/v1_rerun içerisine kaydediliyor. (names, score)

test.py kodu ChatGPT'nin yardımıyla yapıldı. (Python bilgim kısıtlı)
results/liver/point içerisindeki .npy (numpy dosyası) sonuçlarını results_txt içerisine adlarına göre klasörlere ayırıp çeşidine göre .txt ya da .png dosyasına çeviriyor.