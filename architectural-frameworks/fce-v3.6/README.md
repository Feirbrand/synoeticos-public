# FCE v3.6

**Fractal Context Engineering**  
**Multi-Granular Compression | φ-Scaling (Golden Ratio: 1.618)**

## Overview

FCE v3.6 enables multi-granular compression with golden ratio scaling for semantic density optimization.

- **Compression Ratios**: 4-24x depending on mode
- **φ-Scaling**: Golden ratio (1.618) optimization
- **Hurst Exponent**: ~1.6 preservation
- **Entropy Conservation**: 71-89%

## Quick Start

```python
from fce import FCECompressor

fce = FCECompressor()

# Compress with symbolic mode (highest ratio)
result = fce.compress(
    content="Your text here...",
    mode='symbolic',
    target_ratio=8.0
)

print(f"Ratio: {result['compression_ratio']:.1f}x")
print(f"Entropy: {result['entropy_preserved']:.1%}")
```

## Compression Modes

### Symbolic (6-24x)
LLMLingua-style semantic preservation with golden ratio word selection

### Hybrid (4-8x)
CompLLM-style concept preservation with balanced compression

### Flat (4-6x)
EpiCache-style pattern replication for speed-optimized compression

## Research

**Published Paper**: [FCE v3.6](https://zenodo.org/records/17309322)

**ORCID**: 0009-0000-9923-3207

## License

MIT License (implementation code)
CC BY-NC 4.0 (framework architecture)
