# coding=utf-8

# from django.shortcuts import render
from django.http import HttpResponse
import logging
from util.ip import get_client_ip


def statistics_search(request, keyword):
    """Save search info to db
    :param request: HttpRequest
    :param keyword: search key word
    """
    logger = logging.getLogger('clmvp_statistics')
    logger.info('search keyword=%s ip=%s browser=%s' % (keyword, get_client_ip(request), request.META['HTTP_USER_AGENT']))

    return HttpResponse("you are searching %s" % keyword)
