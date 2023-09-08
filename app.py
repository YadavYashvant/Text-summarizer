from flask import Flask ,render_template,request

from summarizer import Summarizer

from summarizer.sbert import SBertSummarizer