from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter


image_filename = "colors.png"


try:
    img = Image.open(image_filename)  # פותח את קובץ התמונה
    img_array = np.array(img)  # ממיר את התמונה למערך NumPy
except FileNotFoundError:
    print(f"Error: The file '{image_filename}' was not found.")  # הדפסת שגיאה אם הקובץ לא נמצא
    exit()  # סיום התוכנית

# שנה את מערך התמונה למערך של פיקסלים (R, G, B)
# reshape(-1, 3) יוצר מערך דו-ממדי שבו כל שורה מייצגת פיקסל ו-3 העמודות מייצגות את ערכי האדום, הירוק והכחול שלו.
pixels = img_array.reshape(-1, 3)

# ספור את הצבעים הנפוצים ביותר (נבחר את 5 המובילים)
# Counter(tuple(p) for p in pixels) סופר את ההופעות של כל צבע (טאפל של R, G, B) ברשימת הפיקסלים.
# most_common(5) מחזיר רשימה של 5 הצבעים הנפוצים ביותר והספירה שלהם.
color_counts = Counter(tuple(p) for p in pixels)
most_common_colors = color_counts.most_common(5)

# הכן נתונים לגרף עוגה
# יצירת רשימה של תוויות לגרף העוגה, המציגות את ערכי ה-RGB של כל צבע.
labels = [f'RGB: {color}' for color, count in most_common_colors]
# יצירת רשימה של גדלים עבור כל פרוסה בעוגה, המייצגים את מספר הפיקסלים של כל צבע.
sizes = [count for color, count in most_common_colors]

# הכן רשימת צבעים בפורמט ש-matplotlib מבין (ערכים בין 0 ל-1).
pie_colors = [(float(r / 255.0), float(g / 255.0), float(b / 255.0)) for (r, g, b), count in most_common_colors]

# הדפס את רשימת הצבעים לבדיקה
print("Pie Colors:", pie_colors)
print("Sizes:", sizes)
print("Labels:", labels)

# צור גרף עוגה
plt.figure(figsize=(8, 8))  # יוצר איור (חלון) חדש עבור הגרף
patches, texts, autotexts = plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, wedgeprops={'edgecolor': 'black'})
# sizes: גדלי הפרוסות
# labels: תוויות לכל פרוסה
# colors: רשימת צבעים לפרוסות (במקרה הזה, לא צובעים את הפרוסות)
# autopct: פורמט להצגת אחוזים על הפרוסות
# startangle: זווית ההתחלה של הפרוסה הראשונה
# wedgeprops: מאפיינים ויזואליים של הפרוסות (במקרה הזה, מוסיפים קו שחור מסביב)

# צבע את המלל של התוויות בצבעים המתאימים
for i, text in enumerate(texts):
    text.set_color(pie_colors[i])  # משנה את צבע הטקסט של כל תוית לצבע המתאים מרשימת הצבעים

plt.title("The top 5 color distribution in the image")  # מגדיר את כותרת הגרף
plt.axis('equal')  # מבטיח שהעוגה מצוירת כעיגול ולא כאליפסה
plt.show()  # מציג את הגרף

# הדפס אנליזה בסיסית
print("\nBasic Analysis:")
for i, (color, count) in enumerate(most_common_colors):
    percentage = (count / len(pixels)) * 100
    print(f"Place {i+1}: RGB color {color} - {count} pixels ({percentage:.2f}%)")