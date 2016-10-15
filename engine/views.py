from django.shortcuts import render
import operator, time
from django.views.decorators.csrf import csrf_exempt
from engine.models import Tag, Image, TagImageScore

# Create your views here.
def home(request):
    try:
        return render(request, 'home.html')
        
    except Exception ,e:
        logging(e)


@csrf_exempt
def search(request):
    try:
        start = time.time()
        query = request.POST.get('query')
        query_words = query.split(' ')
        results = []
        response = {}

        #======Result in only one query with AND clause=======#
        for word in query_words: 
            tag = Tag.objects.get(tag = word)
            results += TagImageScore.objects.filter(tag = tag)

        #====Iterating over returned query for finding strong score results
        for result in results:
            if result.image.url in response:
                response[result.image.url] += result.score
            else:
                response.update({result.image.url: result.score})

        #=======A ranked list of tuple of all images acc to there score
        ranked_response = sorted(response.items(), key=operator.itemgetter(1))

        print 'Execution Time for search algorithm: {}'.format(time.time() - start)
        return JsonResponse({'result': ranked_response})

    except Exception ,e:
        logging(e)


def logging(err):
    print err