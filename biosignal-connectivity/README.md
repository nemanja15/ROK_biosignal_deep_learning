# biosignal-connectivity

Pairwise spectral and phase connectivity for multichannel biosignals.

## Source provenance

[Original project folder](https://drive.google.com/drive/folders/1mAmWRI22mqdwIa32Gt4Txt4i7e54CKWJ). Selected original functions are in `src/`; newly written examples are in `examples/`.

## Usage

MATLAB with Signal Processing Toolbox; MI additionally uses Statistics and Machine Learning Toolbox. Run `examples/demo.m` from the repository root. Inputs are channels × samples. Original functions store upper-triangle entries only. Signed imaginary coherency is not symmetric. MI is experimental: original bin labels and entropy indexing disagree, and `eqpop` requires external `binr`. Do not use MI for inference until fixed.

## Release status

Private review draft. No research data included. Confirm authorship, institutional approval, third-party licenses and numerical validation before public release. No license granted by this draft.
