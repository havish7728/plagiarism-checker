import re
from collections import Counter

def load_text(file_path):
    """Load text from a file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read().lower()

def preprocess_text(text):
    """Normalize text by removing punctuation and splitting into words."""
    return re.sub(r'[^a-zA-Z0-9\s]', '', text).split()

def generate_shingles(words, shingle_size=5):
    """Generate overlapping shingles (substrings) of a fixed size."""
    return [' '.join(words[i:i + shingle_size]) for i in range(len(words) - shingle_size + 1)]

def hash_shingles(shingles):
    """Hash each shingle for efficient comparison."""
    return {hash(shingle) for shingle in shingles}

def calculate_similarity(hash_set1, hash_set2):
    """Calculate Jaccard similarity between two sets of hashes."""
    intersection = len(hash_set1 & hash_set2)
    union = len(hash_set1 | hash_set2)
    return intersection / union if union != 0 else 0

def compare_texts(file1, file2):
    """Compare two text files and return their similarity percentage."""
    text1 = preprocess_text(load_text(file1))
    text2 = preprocess_text(load_text(file2))

    shingles1 = generate_shingles(text1)
    shingles2 = generate_shingles(text2)

    hash_set1 = hash_shingles(shingles1)
    hash_set2 = hash_shingles(shingles2)

    similarity = calculate_similarity(hash_set1, hash_set2)
    return similarity * 100  # Return similarity as a percentage

def compare_with_repository(file, repository):
    """Compare one file against a repository of files."""
    results = {}
    for repo_file in repository:
        similarity = compare_texts(file, repo_file)
        results[repo_file] = similarity
    return results

def highlight_matches(text1, text2):
    """Highlight matching words between two texts."""
    words1 = preprocess_text(text1)
    words2 = preprocess_text(text2)
    common = set(words1) & set(words2)
    highlighted_text1 = ' '.join([f'**{word}**' if word in common else word for word in words1])
    highlighted_text2 = ' '.join([f'**{word}**' if word in common else word for word in words2])
    return highlighted_text1, highlighted_text2

# Example usage
if __name__ == "__main__":
    file1 = "document1.txt"  # Replace with your file paths
    file2 = "document2.txt"

    # Compare two files
    similarity_percentage = compare_texts(file1, file2)
    print(f"Similarity between {file1} and {file2}: {similarity_percentage:.2f}%")
