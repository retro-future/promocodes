# PromoCode Generator

How to set up the project:

* Copy the project using:

```

```

* Go to folder:

```bash
  cd promoGen 
```

---

* Run the command:

```bash
pip install -r requirements.txt
```

Go to the bash and run command:

```bash
python manage.py create_promo 12 "agency"
```
You're going to see the message "successfully added"

To check the promo-codes get any code from "data_file.json" and run the following command:
```bash
python manage.py check_promo <promo_code>
```
If the code exists in the json file you're going to get message "code exists group = {group}"

Running test using:
```bash
python manage.py test
```

