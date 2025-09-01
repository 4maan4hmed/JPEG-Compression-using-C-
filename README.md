# JPEG Compressor

A complete from-scratch implementation of JPEG image compression in C++, demonstrating the full JPEG compression pipeline including DCT transforms, quantization, and Huffman coding.

## 🚀 Quick Start

### Method 1: Terminal/Command Line Usage

**Run the executable directly:**
```bash
./jpeg_compressor input.jpg output.jpg quality
```

**Examples:**
```bash
# High quality compression
./jpeg_compressor Red_peppers.jpg pepper_high_quality.jpg 0.9

# Balanced compression
./jpeg_compressor Red_peppers.jpg pepper_balanced.jpg 0.5  

# High compression (smaller file) - your example
./jpeg_compressor Red_peppers.jpg pepper_compressed.jpg 0.1

# Extreme compression (visible artifacts)
./jpeg_compressor Red_peppers.jpg pepper_extreme.jpg 0.002
```

### Method 2: Web Interface (Streamlit)

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Launch web interface:**
   ```bash
   streamlit run app.py
   ```

3. **Use the web app:**
   - Open browser to `http://localhost:8501`
   - Upload image files (JPG, JPEG, PNG supported)
   - Adjust quality slider (0.002 - 1.0)
   - View compression results and download

### Quality Guide
| Quality | Description | Use Case |
|---------|-------------|----------|
| `1.0` | Best quality, minimal compression | Professional/archival |
| `0.7-0.9` | High quality, moderate compression | Photography |
| `0.3-0.6` | Balanced quality/size | Web images |
| `0.1-0.2` | High compression, visible quality loss | Thumbnails |
| `0.002-0.05` | Extreme compression, significant artifacts | Ultra-low bandwidth |

## 🚀 Features

- **Complete JPEG Pipeline**: Implements all major JPEG compression steps
- **Flexible Quality Control**: Quality range from 0.002 to 1.0 with dynamic quantization
- **Color Space Conversion**: RGB ↔ YCbCr with 4:2:0 chroma subsampling  
- **DCT/IDCT Implementation**: 2D Discrete Cosine Transform for frequency domain processing
- **Huffman Coding**: Dynamic Huffman tree generation based on coefficient distribution
- **Compression Metrics**: Real-time compression ratio reporting
- **Multiple Format Support**: Supports PNG, JPG, BMP input via STB libraries
- **Web Interface**: User-friendly Streamlit interface for interactive compression

## 📁 Project Structure

```
jpeg-compressor/
├── jpeg-cpp.cpp          # Core JPEG compressor source code
├── jpeg_compressor.exe   # Pre-compiled Windows executable
├── app.py               # Streamlit web interface
├── jpeg_wrapper.py      # Python wrapper for executable
├── requirements.txt     # Python dependencies
├── stb_image.h          # Image loading library
├── stb_image_write.h    # Image saving library
└── README.md            # This file
```

## 📋 Prerequisites

- **For Windows**: Nothing! Use the provided `jpeg_compressor.exe`
- **For Linux/Mac**: C++ compiler (g++, clang++) to compile from source
- **For Web Interface**: Python 3.7+ 
- STB image libraries (included in source)

## 🔧 Technical Implementation

### Core Algorithm Steps
1. **Color Space Conversion** - RGB → YCbCr
2. **Chroma Subsampling** - 4:2:0 subsampling for Cb/Cr channels
3. **Block Division** - 8×8 pixel blocks
4. **DCT Transform** - Forward 2D Discrete Cosine Transform
5. **Quantization** - Lossy compression using quality-scaled matrices
6. **Huffman Encoding** - Variable-length coding for efficiency
7. **Reconstruction** - IDCT and YCbCr → RGB conversion

### Key Features
- **Dynamic Quantization**: Quality-adaptive quantization matrices
- **Separable DCT**: Efficient 2D DCT using 1D transforms
- **Probability-Based Huffman**: Trees built from actual coefficient distribution
- **Round-Trip Processing**: Full compression and decompression cycle

## 📊 Performance

### Typical Compression Ratios
- **Quality 0.9**: 3-8:1 compression
- **Quality 0.5**: 10-20:1 compression  
- **Quality 0.1**: 30-60:1 compression
- **Quality 0.002**: 100-300:1 compression

### Sample Output
```
Requested quality: 0.5
Achieved compression ratio: 15.2:1
Compressed image saved to: output.jpg
```

## 🧮 Mathematical Background

### DCT Formula
The 2D DCT transform used:
```
F(u,v) = (1/4) * C(u) * C(v) * Σ Σ f(x,y) * cos[(2x+1)uπ/16] * cos[(2y+1)vπ/16]
```

### Quantization
Coefficients are quantized using:
```
F_quantized(u,v) = round(F(u,v) / Q(u,v))
```

## 🎓 Educational Value

This implementation is designed for:
- **Learning JPEG internals** - Complete, readable implementation
- **Algorithm research** - Modifiable components for experimentation  
- **Performance analysis** - Compression ratio and quality metrics
- **Academic projects** - Well-documented, standards-compliant code

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 References

- [JPEG Standard (ITU-T T.81)](https://www.itu.int/rec/T-REC-T.81)
- [Digital Image Processing - Gonzalez & Woods](https://www.imageprocessingplace.com/)
- [STB Libraries](https://github.com/nothings/stb)

## ⚠️ Notes

- This is an educational implementation optimized for clarity over speed
- For production use, consider optimized libraries like libjpeg or libjpeg-turbo
- Output quality may differ from standard JPEG encoders due to implementation variations

---

**Built with ❤️ for learning and understanding JPEG compression**
