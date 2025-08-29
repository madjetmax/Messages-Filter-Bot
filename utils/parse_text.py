import pymorphy3
import re
import itertools
from typing import Any
from config import *

morph = pymorphy3.MorphAnalyzer(lang="ru")

def normalize(word: str) -> str:
    """normalize word using pymorpht parse() returns first word"""
    normalized_word = morph.parse(word)[0].normal_form

    return normalized_word

def normalize_full(word: str) -> list[str]:
    """normalize word using pymorpht parse() returns list of all word"""
    normalized_words = []

    # add unique normalized words
    for norm_word in morph.parse(word):
        if norm_word.normal_form not in normalized_words:
            normalized_words.append(norm_word.normal_form)
    
    return normalized_words

def has_phrase(normalized_words: list[str], string_phrase: str) -> bool:
    """check if phrase in words list"""
    if string_phrase in "".join(normalized_words):
        return True  
    return False

def check_trigger(text: str, keywords: str, names: list[str], string_phrases: list[str]) -> bool:
    # clear text, parse and normalize words
    text = text.lower()
    raw_words: list = re.findall(r"\w+", text, flags=re.UNICODE)
    
    # * for noramalized words
    # full_normalized_words = list(itertools.chain.from_iterable(raw_normalized_words))
    
    # * checks
    # keywords
    for keyword in keywords:
        in_text = keyword.lower() in raw_words
        if in_text:
            return True
        
        # * with normalize
        # normalized_keyword_options = normalize_full(keyword)
        # # chek every option of keyword
        # for normalized_keyword in normalized_keyword_options:
        #     matches: bool = has_keyword(full_normalized_words, normalized_keyword)
        #     if matches:
        #         parse_results["triggered_dy"] = f'keyword: {keyword}'
        #         return parse_results
        #         # parse_results["keywords"][keyword] = matches
        #         # trigger_found = True
        #         # break
    
    # names
    for name in names:
        in_text = name.lower() in text
        if in_text:
            return True
    
    # phrases
    # normalize text
    raw_normalized_words = list(map(normalize_full, raw_words))
    normalized_words = [words[0] for words in raw_normalized_words]

    for string_phrase in string_phrases:
        contain_phrase: bool = has_phrase(normalized_words, string_phrase)
        if contain_phrase:
            return True

    return False