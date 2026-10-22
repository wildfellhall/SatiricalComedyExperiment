"""
Cell 1: Define corpus and process text
"""

import os
import re
import urllib.request
from datasets import Dataset

urls = [
  "https://www.gutenberg.org/files/1080/1080-0.txt",   # A Modest Proposal by Jonathan Swift
  "https://www.gutenberg.org/files/829/829-0.txt",     # Gulliver's Travels into Several Remote Nations of the World by Jonathan Swift
  "https://www.gutenberg.org/files/4737/4737-0.txt",   # A Tale of a Tub by Jonathan Swift
  "https://www.gutenberg.org/files/1090/1090-0.txt",   # The Bickerstaff-Partridge Papers by Jonathan Swift
  "https://www.gutenberg.org/files/121/121-0.txt",     # Northanger Abbey by Jane Austen
  "https://www.gutenberg.org/files/86/86-0.txt",       # A Connecticut Yankee in King Arthur's Court by Mark Twain
  "https://www.gutenberg.org/files/599/599-0.txt",     # Vanity Fair by William Makepeace Thackeray
  "https://www.gutenberg.org/files/3178/3178-0.txt",   # The Gilded Age: A Tale of Today by Mark Twain and Charles Dudley Warner
  "https://www.gutenberg.org/files/883/883-0.txt",     # Our Mutual Friend by Charles Dickens
  "https://www.gutenberg.org/files/1906/1906-0.txt",   # Erewhon; Or, Over the Range by Samuel Butler
  "https://www.gutenberg.org/files/4558/4558-0.txt",   # Barry Lyndon by William Makepeace Thackeray
  "https://www.gutenberg.org/files/897/897-0.txt",     # The Rose and the Ring by William Makepeace Thackeray
  "https://www.gutenberg.org/files/2686/2686-0.txt",   # The Book of Snobs by William Makepeace Thackeray
  "https://www.gutenberg.org/files/2675/2675-0.txt",   # Burlesques by William Makepeace Thackeray
  "https://www.gutenberg.org/files/2731/2731-0.txt",   # The Christmas Books of Mr. M.A. Titmarsh by William Makepeace Thackeray
  "https://www.gutenberg.org/files/2844/2844-0.txt",   # The Fatal Boots by William Makepeace Thackeray
  "https://www.gutenberg.org/files/2823/2823-0.txt",   # The Fitz-Boodle Papers by William Makepeace Thackeray
  "https://www.gutenberg.org/files/2796/2796-0.txt",   # The Memoirs of Mr. Charles J. Yellowplush by William Makepeace Thackeray
  "https://www.gutenberg.org/files/1935/1935-0.txt",   # The Tremendous Adventures of Major Gahagan by William Makepeace Thackeray
  "https://www.gutenberg.org/files/2859/2859-0.txt",   # A Little Dinner at Timmins's by William Makepeace Thackeray
  "https://www.gutenberg.org/files/61072/61072-0.txt", # "Our Street" by William Makepeace Thackeray
  "https://www.gutenberg.org/files/20001/20001-0.txt", # The English spy : an original work characteristic, satirical, and humorous.…
  "https://www.gutenberg.org/files/19942/19942-0.txt", # Candide by Voltaire
  "https://www.gutenberg.org/files/1081/1081-0.txt",   # Dead Souls by Nikolai Vasilevich Gogol
  "https://www.gutenberg.org/files/45858/45858-0.txt", # Lucian's True History by of Samosata Lucian
  "https://www.gutenberg.org/files/10430/10430-0.txt", # Trips to the Moon by of Samosata Lucian
  "https://www.gutenberg.org/files/968/968-0.txt",     # Martin Chuzzlewit by Charles Dickens
  "https://www.gutenberg.org/files/652/652-0.txt",     # Rasselas, Prince of Abyssinia by Samuel Johnson
  "https://www.gutenberg.org/files/44520/44520-0.txt", # Pamphlets and Parodies on Political Subjects by William Hone
  "https://www.gutenberg.org/files/5231/5231-0.txt",   # The Way We Live Now by Anthony Trollope
  "https://www.gutenberg.org/files/619/619-0.txt",     # The Warden by Anthony Trollope
  "https://www.gutenberg.org/files/7381/7381-0.txt",   # The Eustace Diamonds by Anthony Trollope
  "https://www.gutenberg.org/files/27533/27533-0.txt", # The Struggles of Brown, Jones, and Robinson by Anthony Trollope
  "https://www.gutenberg.org/files/21816/21816-0.txt", # The Confidence-Man: His Masquerade by Herman Melville
  "https://www.gutenberg.org/files/6053/6053-0.txt",   # Evelina, Or, the History of a Young Lady's Entrance into the World by Fanny Burney
  "https://www.gutenberg.org/files/1051/1051-0.txt",   # Sartor Resartus: The Life and Opinions of Herr Teufelsdröckh by Thomas Carlyle
  "https://www.gutenberg.org/files/3190/3190-0.txt",   # 1601: Conversation as it was by the Social Fireside in the Time of the Tudors
  "https://www.gutenberg.org/files/3172/3172-0.txt",   # Fenimore Cooper's Literary Offences by Mark Twain
  "https://www.gutenberg.org/files/21822/21822-0.txt", # A Lecture On Heads by George Alexander Stevens
  "https://www.gutenberg.org/files/10095/10095-0.txt", # The Twilight of the Gods, and Other Tales by Richard Garnett
  "https://www.gutenberg.org/files/6758/6758-0.txt",   # The Adventures of Sir Launcelot Greaves by T. Smollett
  "https://www.gutenberg.org/files/6761/6761-0.txt",   # The Adventures of Ferdinand Count Fathom — Complete by T. Smollett
  "https://www.gutenberg.org/files/4092/4092-0.txt",   # The Monikins by James Fenimore Cooper
  "https://www.gutenberg.org/files/2329/2329-0.txt",   # Autobiography of a Pocket-Handkerchief by James Fenimore Cooper
  "https://www.gutenberg.org/files/2615/2615-0.txt",   # Discourses on Satire and on Epic Poetry by John Dryden
  "https://www.gutenberg.org/files/1473/1473-0.txt",   # The Absentee by Maria Edgeworth
  "https://www.gutenberg.org/files/21337/21337-0.txt", # 'That Very Mab' by May Kendall and Andrew Lang
  "https://www.gutenberg.org/files/38411/38411-0.txt", # Froth: A Novel by Armando Palacio Valdés
  "https://www.gutenberg.org/files/9909/9909-0.txt",   # Nightmare Abbey by Thomas Love Peacock
  "https://www.gutenberg.org/files/2075/2075-0.txt",   # Crotchet Castle by Thomas Love Peacock
  "https://www.gutenberg.org/files/1079/1079-0.txt",   # The life and opinions of Tristram Shandy, gentleman by Laurence Sterne
  "https://www.gutenberg.org/files/804/804-0.txt",     # A Sentimental Journey Through France and Italy by Laurence Sterne
  "https://www.gutenberg.org/files/20257/20257-0.txt", # A Political Romance by Laurence Sterne
  "https://www.gutenberg.org/files/58070/58070-0.txt", # Home Life in Russia, Volumes 1 and 2 by Nikolai Vasilevich Gogol
  "https://www.gutenberg.org/files/46621/46621-0.txt", # Sheppard Lee, Written by Himself. Vol. 1 (of 2) by Robert Montgomery Bird
  "https://www.gutenberg.org/files/46622/46622-0.txt", # Sheppard Lee, Written by Himself. Vol. 2 (of 2) by Robert Montgomery Bird
  "https://www.gutenberg.org/files/12793/12793-0.txt", # Cobwebs from an Empty Skull by Ambrose Bierce
  "https://www.gutenberg.org/files/4793/4793-0.txt",   # The Fiend's Delight by Ambrose Bierce
  "https://www.gutenberg.org/files/55035/55035-0.txt", # The Marvellous Adventures and Rare Conceits of Master Tyll Owlglass by Mackenzie et al.
  "https://www.gutenberg.org/files/67888/67888-0.txt", # Anticipation by Richard Tickell
  "https://www.gutenberg.org/files/39726/39726-0.txt", # The Rolliad, in Two Parts by Tickell, Ellis, Laurence, and Richardson
  "https://www.gutenberg.org/files/46467/46467-0.txt", # The Remarkable History of Sir Thomas Upmore, bart., M.P., formerly known as…
  "https://www.gutenberg.org/files/3191/3191-0.txt",   # Goldsmith's Friend Abroad Again by Mark Twain
  "https://www.gutenberg.org/files/19484/19484-0.txt", # Editorial Wild Oats by Mark Twain
  "https://www.gutenberg.org/files/60900/60900-0.txt", # Merry Tales by Mark Twain
  "https://www.gutenberg.org/files/30343/30343-0.txt", # A discourse concerning ridicule and irony in writing (1729) by Anthony Collins
  "https://www.gutenberg.org/files/41950/41950-0.txt", # The Visions of Quevedo by Francisco de Quevedo
  "https://www.gutenberg.org/files/46125/46125-0.txt", # Pablo de Segovia, the Spanish Sharper by Francisco de Quevedo
  "https://www.gutenberg.org/files/75943/75943-0.txt", # Melincourt : or, Sir Oran Haut-Ton by Thomas Love Peacock
  "https://www.gutenberg.org/files/47427/47427-0.txt", # The Dance of Death by William Herman
  "https://www.gutenberg.org/files/21514/21514-0.txt", # Gryll Grange by Thomas Love Peacock
  "https://www.gutenberg.org/files/12803/12803-0.txt", # Headlong Hall by Thomas Love Peacock
  "https://www.gutenberg.org/files/7089/7089-0.txt",   # The Consolidator; or, Memoirs of Sundry Transactions from the World in the Moon
  "https://www.gutenberg.org/files/6453/6453-0.txt",   # The Potiphar Papers by George William Curtis
  "https://www.gutenberg.org/files/66123/66123-0.txt", # Pictures of the Socialistic Future by Eugen Richter
  "https://www.gutenberg.org/files/73620/73620-0.txt", # The island : or, an adventure of a person of quality by Richard Whiteing
  "https://www.gutenberg.org/files/23390/23390-0.txt", # The True Life of Betty Ireland by Anonymous
  "https://www.gutenberg.org/files/2164/2164-0.txt",   # The Lumley Autograph by Susan Fenimore Cooper
  "https://www.gutenberg.org/files/77997/77997-0.txt", # Uncle Tweazy and his quizzical neighbours, vol. 1 of 3 : a comi-satiric novel
  "https://www.gutenberg.org/files/77028/77028-0.txt", # Uncle Tweazy and his quizzical neighbours, vol. 2 of 3 : a comi-satiric novel
  "https://www.gutenberg.org/files/26481/26481-0.txt", # The Romance of Mathematics by P. H. Ditchfield
  "https://www.gutenberg.org/files/623/623-0.txt",     # The Battle of the Books, and other Short Pieces by Jonathan Swift
  "https://www.gutenberg.org/files/5225/5225-0.txt",   # The Satyricon — Complete by Petronius Arbiter
  "https://www.gutenberg.org/files/581/581-0.txt",     # Ginx's Baby: His Birth and Other Misfortunes; a Satire by Edward Jenkins
  "https://www.gutenberg.org/files/28105/28105-0.txt", # A Learned Dissertation on Dumpling (1726) by Henry Carey
  "https://www.gutenberg.org/files/39119/39119-0.txt", # Satires and Profanities by James Thomson and G. W. Foote
  "https://www.gutenberg.org/files/51017/51017-0.txt", # Anecdotes of the Learned Pig by James Boswell and Hester Lynch Piozzi
  "https://www.gutenberg.org/files/68133/68133-0.txt", # The history of the proceedings in the case of Margaret, commonly called Peg,…
  "https://www.gutenberg.org/files/29189/29189-0.txt", # A Letter From a Clergyman to his Friend, by Anonymous
  "https://www.gutenberg.org/files/31155/31155-0.txt", # The Academy Keeper by Anonymous
  "https://www.gutenberg.org/files/70039/70039-0.txt", # First harvests : An episode in the life of Mrs. Levison Gower : A satire…
  "https://www.gutenberg.org/files/158/158-0.txt",     # Emma by Jane Austen
  "https://www.gutenberg.org/files/1342/1342-0.txt",   # Pride and Prejudice by Jane Austen
  "https://www.gutenberg.org/files/75845/75845-0.txt", # The genuine tryal of Dr. Nosmoth, a physician in Pekin : For the murder of the…
  "https://www.gutenberg.org/files/75432/75432-0.txt", # An account of the giants lately discovered : In a letter to a friend in the…
  "https://www.gutenberg.org/files/78245/78245-0.txt", # The Mudfog papers, etc. by Charles Dickens
  "https://www.gutenberg.org/files/69793/69793-0.txt", # Caught napping by Anonymous
  "https://www.gutenberg.org/files/76013/76013-0.txt", # Honesty the best policy : or, The history of Roger by Anonymous
  "https://www.gutenberg.org/files/996/996-0.txt",     # Don Quixote by Miguel de Cervantes Saavedra
  "https://www.gutenberg.org/files/1200/1200-0.txt",   # Gargantua and Pantagruel by François Rabelais
]

def expurgate_gutenberg(text):
    # 1. Strip Legal License Headers and Footers
    start_match = re.search(r"\*\*\*\s*START OF TH(IS|E) PROJECT GUTENBERG EBOOK.*?\*\*\*", text, re.IGNORECASE)
    end_match = re.search(r"\*\*\*\s*END OF TH(IS|E) PROJECT GUTENBERG EBOOK.*?\*\*\*", text, re.IGNORECASE)
    
    if start_match and end_match:
        text = text[start_match.end():end_match.start()]
    elif start_match:
        text = text[start_match.end():]

    # 2. Expurgate Transcriber Notes, Annotations, and Bracketed Metadata
    text = re.sub(r"\[Transcriber'?s?\s*Note:?.*?\]", "", text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r"\[Illustration:?.*?\]", "", text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r"\[Footnote:?.*?\]", "", text, flags=re.IGNORECASE | re.DOTALL)

    # 3. Strip Chapter Headings, Roman Numerals, and Section Headers
    text = re.sub(r"^\s*(CHAPTER|BOOK|VOLUME|PART|SECTION|CANTO|ACT|SCENE)\s+([0-9IVXLCDM]+|\w+)\b.*$", "", text, flags=re.IGNORECASE | re.MULTILINE)
    text = re.sub(r"^\s*[IVXLCDM]{1,10}\.\s*$", "", text, flags=re.MULTILINE)

    # 4. Remove Publisher Colophons, Printers, and Gutenberg Archive Metadata
    text = re.sub(r"Printed by\s+.*$", "", text, flags=re.IGNORECASE | re.MULTILINE)
    text = re.sub(r"London\s*:\s*Published by\s+.*$", "", text, flags=re.IGNORECASE | re.MULTILINE)
    text = re.sub(r"End of (the )?Project Gutenberg EBook.*$", "", text, flags=re.IGNORECASE | re.MULTILINE)

    # 5. Normalize Typography and Excessive Whitespace
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]+", " ", text)
    
    return text.strip()

cleaned_texts = []
print("Downloading and sanitizing corpus...")

for url in urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            raw_content = response.read().decode('utf-8-sig', errors='ignore')
            sanitized = expurgate_gutenberg(raw_content)
            if len(sanitized) > 1000:  # Valid text check
                cleaned_texts.append(sanitized)
    except Exception as e:
        print(f"Skipping {url} due to error: {e}")

print(f"Successfully processed {len(cleaned_texts)} works.")

# Save raw merged text for Tokenizer training
with open("sanitized_satire_corpus.txt", "w", encoding="utf-8") as f:
    f.write("\n\n<|endoftext|>\n\n".join(cleaned_texts))

"""
Cell 2: Train custom tokenizer
"""
import os
from tokenizers import ByteLevelBPETokenizer
from transformers import PreTrainedTokenizerFast

# Train a 12,288 vocab tokenizer (Saves embedding parameters)
special_tokens = ["<|endoftext|>", "<|pad|>"]

bpe_tokenizer = ByteLevelBPETokenizer()
bpe_tokenizer.train(
    files=["sanitized_satire_corpus.txt"],
    vocab_size=12288,
    min_frequency=2,
    special_tokens=special_tokens
)

os.makedirs("satire_tokenizer", exist_ok=True)
bpe_tokenizer.save_model("satire_tokenizer")

tokenizer = PreTrainedTokenizerFast(
    tokenizer_file="satire_tokenizer/vocab.json",
    vocab_file="satire_tokenizer/vocab.json",
    merges_file="satire_tokenizer/merges.txt",
    bos_token="<|endoftext|>",
    eos_token="<|endoftext|>",
    pad_token="<|pad|>"
)
