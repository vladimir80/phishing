import logging
import config
from cache import URLCache
from result import Result
from learn import Learner
from feature_extraction import FeatureExtractor

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class PhishDetector:
    def __init__(self):
        self.white_cache = None
        self.black_cache = None
        self.learner = None

        self.use_w = config.USE_WHITE_LIST
        self.use_b = config.USE_BLACK_LIST
        self.use_ml = config.USE_ML

        if self.use_w:
            self.white_cache = URLCache(config.WHITE_LIST)

        if self.use_b:
            self.black_cache = URLCache(config.BLACK_LIST)

        if self.use_ml:
            self.learner = Learner(config.LEARNER_PATH)

    def detect_url(self, url):
        if self.use_w and self.white_cache.check(url):
            return Result(phase=config.WHITE_LIST, param=url)

        logger.info('white phase is {} and url not found'.format(self.use_w))

        if self.use_b and self.black_cache.check(url):
            return Result(phase=config.WHITE_LIST, param=url)

        logger.info('black phase is {} and url not found'.format(self.use_w))

        if self.use_ml:
            vector = FeatureExtractor.get_vector(url=url)
            proba = self.learner.predict_proba(vector)
            return Result(phase=config.RESULT_ML, param=proba)

        logger.info('ML phase is SKIPPED')

        # All filters are disabled or url not found in caches
        return Result(phase=config.RESULT_SKIP, param=None)


if __name__ == '__main__':
    detector = PhishDetector()
    url1 = 'www.google.com'
    result = detector.detect_url(url1)
    logger.info('Result of site {}:\n PHASE {} - PROBABILITY {}'.format(url1, result.phase, result.param))