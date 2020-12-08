import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/src/backer-1585550181964-0c56f7cc1569.json"
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "backer-1585550181964-0c56f7cc1569.json"


def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')

    for text in texts:
        print('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        print('bounds: {}'.format(','.join(vertices)))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    result = []
    for text in texts:
        vertices = text.bounding_poly.vertices
        vertices = [[vertex.x, vertex.y] for vertex in vertices]
        result.append({'text': text.description, 'vertices': vertices})
#     texts = [text.description for text in texts]
#     return {'texts':texts}
    return result
#     print('Texts:')
# 
#     for text in texts:
#         print('\n"{}"'.format(text.description))
# 
#         vertices = (['({},{})'.format(vertex.x, vertex.y)
#                     for vertex in text.bounding_poly.vertices])
# 
#         print('bounds: {}'.format(','.join(vertices)))
# 
#     if response.error.message:
#         raise Exception(
#             '{}\nFor more info on error messages, check: '
#             'https://cloud.google.com/apis/design/errors'.format(
#                 response.error.message))



def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    blocks = response.full_text_annotation.pages[0].blocks
    result = []
    for block in blocks:
        text_result = ''
        for paragraph in block.paragraphs:
            for word in paragraph.words:
                for symbol in word.symbols:
                  text_result = text_result + symbol.text
      
      
        block_result = {}
        block_result['text'] = text_result  
        thing = block.bounding_box.vertices[0] 
        vertices = {'x': thing.x, 'y': thing.y}
        block_result['vertices'] = vertices
        result.append(block_result)
    return result


# def together(n):
#   block = response.full_text_annotation.pages[0].blocks[n]
#   result = ''
#   for paragraph in block.paragraphs:
#     for word in paragraph.words:
#       for symbol in word.symbols:
#         result = result + symbol.text
#   return result





# print(detect_text('frames/frame.jpg'))