import cv2
import sys
from pathlib import Path

# Adjust path
sys.path.append(str(Path(__file__).resolve().parent))

from src.detector import LicensePlateDetector
from src.quantum_edge import QuantumEdgeDetector
from src.main import crop_plate
from src.segmentation import segment_characters
from src.preprocessing import calculate_blur, preprocess_for_ocr
from src.ocr import ExpertOCR

# Load image
image_path = 'sample_car_real.jpg'
image = cv2.imread(image_path)

if image is None:
    print(f"Failed to load {image_path}")
    exit(1)

# Detect plate
detector = LicensePlateDetector()
expert_ocr = ExpertOCR()
detections = detector.detect(image)

print(f"Detections: {len(detections)}")

q_edge = QuantumEdgeDetector()

for i, bbox in enumerate(detections):
    plate_img = crop_plate(image, bbox)
    
    cv2.imwrite(f'plate_{i}.jpg', plate_img)
    
    blur_score = calculate_blur(plate_img)
    is_blurry = blur_score < 100.0
    
    preprocessed_plate = preprocess_for_ocr(plate_img) if is_blurry else plate_img
    cv2.imwrite(f'preprocessed_{i}.jpg', preprocessed_plate)
    
    preprocessed_plate_bgr = cv2.cvtColor(preprocessed_plate, cv2.COLOR_GRAY2BGR) if len(preprocessed_plate.shape) == 2 else preprocessed_plate
        
    edges_img = q_edge.detect_edges(preprocessed_plate_bgr)
    
    # Run full OCR on the enhanced plate for ground truth / baseline
    full_text_results = expert_ocr.detect_with_box(preprocessed_plate_bgr)
    print(f"Full Plate OCR: {full_text_results}")
    
    chars = segment_characters(preprocessed_plate_bgr)
    
    print(f"Segmented characters: {len(chars)}")
    
    # Try classifying each char individually
    recognized = ""
    for j, char in enumerate(chars):
        # easyocr expects BGR image usually, char is likely binary or gray
        if len(char.shape) == 2:
            char_bgr = cv2.cvtColor(char, cv2.COLOR_GRAY2BGR)
        else:
            char_bgr = char
            
        # pad char a bit for better OCR
        char_padded = cv2.copyMakeBorder(char_bgr, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=[255,255,255] if char_bgr.mean() > 127 else [0,0,0])
        res = expert_ocr.predict(char_padded)
        print(f"Char {j} OCR: {res}")
        if res:
            recognized += res[0]
        else:
            recognized += "?"
            
    print(f"Individual Characters appended: {recognized}")

print("Test complete.")
