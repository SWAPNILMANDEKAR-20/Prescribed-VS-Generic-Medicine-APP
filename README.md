Generic vs Prescribed Medicine App
<img width="350" height="500" alt="image" src="https://github.com/user-attachments/assets/b8f32918-8b15-473b-8b9d-56a685ef02d2" />


Overview
The Generic vs Prescribed Medicine App is designed to help users easily find **generic alternatives** to costly branded medications. It promotes affordable healthcare access by offering detailed information such as **drug usage**, **price comparisons**, and **side effects**, all sourced from reliable databases like the **OpenFDA API**.


Features
- Search Functionality: Enter the name of a branded medicine and retrieve its generic counterpart.
- Price Comparison: Know how much you can save by switching to a generic option.
- Detailed View: Displays usage, side effects, and generic names.
- Caching: Stores frequent searches for faster access.
- User-Friendly Interface: Easy navigation for all user groups.
- Real-Time Data Integration: Fetches the latest information from the OpenFDA database.



Technologies Used

Backend:
- Python: Core logic and data handling
- Flask (or Django): Web framework for API endpoints and routing
- OpenFDA API: Source for drug data including generic-brand mappings

Frontend:
- HTML, CSS, JavaScript
- Bootstrap: For responsive UI
- React *(optional enhancement)*: For a more interactive SPA (Single Page Application)



Project Structure

![image](https://github.com/user-attachments/assets/22db40cd-a50b-4321-9c14-5a5011d168aa)


How to Use

1. Clone the repository
git clone (https://github.com/SWAPNIL-20-MANDEKAR>/generic-vs-prescribed-medicine-app
)
cd generic-vs-prescribed-medicine-app


2. Install dependencies 
pip install -r requirements.txt


3. Run the app
python app.py


4. Open your browser and visit:  

http://127.0.0.1:5000


5. Search for a medicine  
- Type the name of a prescribed/branded medicine (e.g., `Lipitor`)
- The app will return its generic form (e.g., `Atorvastatin`) with price and side effects



 Use Case

A user prescribed an expensive drug like **Moxatag** can enter the name in the app. The app fetches and shows **Amoxicillin** as a generic substitute, listing its use, price, and known side effects.

License
This project is intended for educational and research purposes only. Usage of third-party APIs or models is subject to their individual licenses.



