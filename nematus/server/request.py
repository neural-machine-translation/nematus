#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Defines the abstract request format for Nematus server.
"""

from abc import ABCMeta, abstractmethod
import uuid

class TranslationRequest(object):
    """
    Abstract translation request base class.
    """
    __metaclass__ = ABCMeta

    def __init__(self, request):
        """
        Initialises a translation request.

        @type raw_body: str
        @param raw_body: the POST request submitted to Nematus server.
        """
        self._request = request
        self.request_id = str(uuid.uuid4())
        self.segments = []
        self.beam_width = 5
        self.normalize = True
        self.char_level = False
        self.n_best = 1
        self.suppress_unk = False
        self.get_alignment = False
        self.return_word_probabilities = False
        self._parse()

    @abstractmethod
    def _format(self):
        """
        Formats this translation response.
        """
        pass # to be implemented in subclasses

    def __repr__(self):
        """
        Returns the raw body of this translation request.
        """
        return self._format()

    @abstractmethod
    def _parse(self):
        """
        Parses the request's raw body. Sets or overrides
        * self.segments
        * self.beam_width
        * self.normalize
        * self.character_level
        * self.n_best
        * self.suppress_unk
        * self.return_word_alignment
        * self.return_word_probabilities
        """
        pass # to be implemented in subclasses
