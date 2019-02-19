
def test_get_company_valid(client):
    response = client.get("api/companies/bugsall")

    assert response.status_code == 200
    assert response.json == {
                            "company": "BUGSALL",
                            "index": 4
                            }

def test_company_invalid_data(client):
    response =client.get("api/companies/xyz")
    assert response.status_code ==404
    assert response.json =={"message":"Requested Company not found"}


def test_people_in_invalid_company(client):
    response =client.get("api/people/company/xyz")
    assert response.status_code ==404
    assert response.json =={"message":"Requested Company not found"}


def test_people_in_valid_company(client):
    response =client.get("api/people/company/zolarity")
    assert response.status_code ==200
    assert response.json ==[{"age": 61,"email": "tammylowery@earthmark.com","index": 36,"name": "Tammy Lowery","phone": "+1 (910) 566-2351"},{"age": 54,"email": "marciharvey@earthmark.com","index": 48,"name": "Marci Harvey","phone": "+1 (819) 581-2642"},{"age": 57,"email": "browningweaver@earthmark.com","index": 213,"name": "Browning Weaver","phone": "+1 (951) 434-3469"},{"age": 50,"email": "gaycampos@earthmark.com","index": 247,"name": "Gay Campos","phone": "+1 (944) 556-2480"},{"age": 21,"email": "karenbanks@earthmark.com","index": 310,"name": "Karen Banks","phone": "+1 (807) 551-2285"},{"age": 63,"email": "marshastevenson@earthmark.com","index": 401,"name": "Marsha Stevenson","phone": "+1 (838) 436-2315"},{"age": 64,"email": "diannefinley@earthmark.com","index": 410,"name": "Dianne Finley","phone": "+1 (969) 503-2712"},{"age": 30,"email": "bondstokes@earthmark.com","index": 471,"name": "Bond Stokes","phone": "+1 (895) 435-3302"},{"age": 53,"email": "perryherman@earthmark.com","index": 529,"name": "Perry Herman","phone": "+1 (834) 482-2258"},{"age": 46,"email": "haleybates@earthmark.com","index": 820,"name": "Haley Bates","phone": "+1 (852) 576-3055"},{"age": 22,"email": "dianaburgess@earthmark.com","index": 891,"name": "Diana Burgess","phone": "+1 (813) 477-2758"}]

def test_people_mutual_friends_present(client):
    response =client.get("api/people/mutual_friends/Bonnie Bass/Grace Kelly")
    assert response.status_code ==200
    assert response.json =={ "mutual_friends": [ { "age": 60, "email": "deckermckenzie@earthmark.com", "index": 1, "name": "Decker Mckenzie", "phone": "+1 (893) 587-3311" } ], "person_2": { "age": 24, "email": "gracekelly@earthmark.com", "index": 5, "name": "Grace Kelly", "phone": "+1 (923) 600-2868" }, "person_1": { "age": 54, "email": "bonniebass@earthmark.com", "index": 2, "name": "Bonnie Bass", "phone": "+1 (823) 428-3710" } };


def test_people_mutual_friends_invalid_data(client):
    response =client.get("api/people/mutual_friends/xyz/abcdefda")
    assert response.status_code ==404
    assert response.json =={ "message": "xyz and abcdefda are not citizens of Paranura"}


def test_people_fav_food_valid_data(client):
    response =client.get("api/people/fav_food/Bonnie Bass")
    assert response.status_code ==200
    assert response.json =={ "age": 54, "fruits": [ "orange", "banana", "strawberry" ], "user_name": "Bonnie Bass", "vegetables": [ "beetroot" ] };


def test_people_fav_food_invalid_data(client):
    response =client.get("api/people/fav_food/xyzabc")
    assert response.status_code ==404
    assert response.json =={ "message": "xyzabc is not a citizen of Paranura"}


