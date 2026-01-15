# AI Solutions Consultant

A beautiful, modern AI consulting web app that analyzes company descriptions using Google's Gemini AI and provides structured business recommendations.

## Features

✨ **Stunning UI Design**
- Aqua and light green color scheme with gradient effects
- Light/Dark mode toggle with persistent preference
- Animated background particles and smooth transitions
- Responsive design for mobile and desktop
- Modern glassmorphism effects

🤖 **AI-Powered Analysis**
- Powered by Google Gemini 2.0 Flash
- Structured output with:
  - Top 3 business problems
  - 3 demo/prototype ideas
  - Email opener tailored to the company

🎨 **User Experience**
- Copy-to-clipboard functionality
- Print-friendly results page
- Smooth animations and transitions
- Clean, professional interface

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install individually:
```bash
pip install Flask google-generativeai
```

### 2. Configure API Key

Your Gemini API key is already configured in the `app.py` file. If you need to change it:

1. Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Update the key in `app.py` line 7:
   ```python
   genai.configure(api_key="YOUR_API_KEY_HERE")
   ```

### 3. Run the Application

```bash
python app.py
```

The app will start on `http://localhost:5001`

### 4. Use the Application

1. Open your browser to `http://localhost:5001`
2. Paste a company description or notes
3. Click "Analyze Company"
4. View the AI-generated recommendations
5. Toggle between light/dark mode as preferred
6. Copy results or print them for sharing

## Project Structure

```
├── app.py                 # Flask application with Gemini integration
├── templates/
│   ├── form.html         # Main input form with stunning UI
│   └── ai_result.html    # Results page with AI recommendations
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (API key)
└── README.md            # This file
```

## Design Features

### Color Palette

**Dark Mode:**
- Primary Background: Deep blue (#0a1628)
- Accents: Aqua (#00d9ff) and Neon Green (#00ff9f)
- Gradients: Aqua to green transitions

**Light Mode:**
- Primary Background: Light cyan (#e8f9fa)
- Accents: Ocean blue (#0099cc) and Teal green (#00cc7a)
- Softer gradient variations

### Typography
- **Headers:** Orbitron (futuristic, tech-focused)
- **Body:** Poppins (clean, readable)
- **Code:** Fira Code (monospace for AI output)

### Animations
- Floating background particles
- Smooth page transitions
- Hover effects on buttons and cards
- Glowing effects on headers
- Staggered content reveal

## Troubleshooting

### API Key Issues
- Ensure your Gemini API key is valid
- Check that you have API credits available
- Verify the key is correctly set in `app.py`

### Port Already in Use
If port 5001 is occupied, change it in `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5002)
```

### Module Not Found
Make sure all dependencies are installed:
```bash
pip install -r requirements.txt
```

## API Reference

The app uses:
- **Flask** for web framework
- **Google Generative AI** (Gemini) for AI analysis
- **Gemini 2.0 Flash** model for fast, efficient responses

## License

This project uses the Gemini API and follows Google's terms of service.

## Credits

Designed with modern UI/UX principles inspired by contemporary design systems and Figma best practices.
