from .lazyloader import LazyLoader

__all__ = ['complicated']

complicated = LazyLoader('complicated', globals(), 'tflazyload.complicated')