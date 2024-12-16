
# Image 1
curl -X POST http://localhost:5000/api/v1/ad-quality \
-H "Content-Type: application/json" \
-d '{
    "id": 1,
    "image_url": "https://sandbox.lemmatechnologies.com/media/1080/1733224888644237689-pngimg.com%20-%20skull_PNG70.png"
}'

# Image 2
curl -X POST http://localhost:5000/api/v1/ad-quality \
-H "Content-Type: application/json" \
-d '{
    "id": 2,
    "image_url": "https://sandbox.lemmatechnologies.com/media/1080/1733383990920810264-Screenshot%20from%202024-11-18%2011-50-42.png"
}'


# Image 3
curl -X POST http://localhost:5000/api/v1/ad-quality \
-H "Content-Type: application/json" \
-d '{
    "id": 3,
    "image_url": "https://sandbox.lemmatechnologies.com/media/1080/1733390872843905792-Screenshot%20from%202024-11-29%2017-25-55.png"
}'

# Image 4
curl -X POST http://localhost:5000/api/v1/ad-quality \
-H "Content-Type: application/json" \
-d '{
    "id": 4,
    "image_url": "https://sandbox.lemmatechnologies.com/media/1080/20240731070010-thumbnail-20240730125117-20230718114610-Motorola_RD_1080x1920_30June_2.jpg"
}'

# Image 5
curl -X POST http://localhost:5000/api/v1/ad-quality \
-H "Content-Type: application/json" \
-d '{
    "id": 5,
    "image_url": "https://sandbox.lemmatechnologies.com/media/1080/20240731091842-Screenshot%20from%202024-07-25%2012-40-50.png"
}'
