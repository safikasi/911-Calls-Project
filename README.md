<h1>🚨 911 Emergency Calls — Data Analysis & Visualization</h1>

<p>
  <img src="https://img.shields.io/badge/status-completed-brightgreen" />
  <img src="https://img.shields.io/badge/python-3.8%2B-blue" />
  <img src="https://img.shields.io/badge/visualization-seaborn%20%7C%20matplotlib-ff69b4" />
</p>

<p>
  A <strong>data analysis & visualization project</strong> exploring real-world 911 emergency calls from <strong>Montgomery County, Pennsylvania</strong>.<br>
  This project uncovers insightful trends & patterns in emergency services usage across <strong>time, type, and location</strong>, presented through impactful visualizations.
</p>

<hr>

<h2>🎯 Objectives</h2>
<ul>
  <li>✅ Identify the <strong>most common emergency types</strong> (Traffic, EMS, Fire)</li>
  <li>✅ Detect <strong>peak hours & days</strong> for calls</li>
  <li>✅ Analyze <strong>monthly & daily trends</strong></li>
  <li>✅ Visualize patterns using advanced plots:
    <ul>
      <li>📊 Countplots</li>
      <li>📈 Time series</li>
      <li>🔥 Heatmaps & Clustermaps</li>
    </ul>
  </li>
</ul>

<hr>

<h2>📁 Dataset</h2>
<ul>
  <li><strong>Source:</strong> <a href="https://www.kaggle.com/mchirico/montcoalert">911 Calls Dataset — Kaggle</a></li>
  <li><strong>Size:</strong> ~50,000+ records</li>
  <li><strong>Features:</strong>
    <ul>
      <li><code>lat</code>, <code>lng</code>: Location coordinates</li>
      <li><code>desc</code>: Call description</li>
      <li><code>zip</code>, <code>twp</code>: ZIP code & township</li>
      <li><code>title</code>: Emergency reason</li>
      <li><code>timeStamp</code>: Call time</li>
      <li><code>e</code>: Dummy column</li>
    </ul>
  </li>
</ul>

<hr>

<h2>🔍 Key Insights</h2>
<ul>
  <li>🚗 <strong>Traffic-related emergencies</strong> are the most frequent</li>
  <li>🕓 Most calls occur during <strong>work hours & weekdays</strong></li>
  <li>📅 Noticeable <strong>monthly spikes & daily patterns</strong></li>
  <li>🔥 <strong>Heatmaps</strong> highlight hotspots by hour & day</li>
</ul>

<hr>

<h2>🛠️ Tools & Libraries</h2>

<table>
  <thead>
    <tr>
      <th>Library</th>
      <th>Purpose</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><code>pandas</code></td><td>Data wrangling & preprocessing</td></tr>
    <tr><td><code>numpy</code></td><td>Numerical operations</td></tr>
    <tr><td><code>matplotlib</code></td><td>Visualization</td></tr>
    <tr><td><code>seaborn</code></td><td>Advanced, beautiful plots</td></tr>
  </tbody>
</table>

<hr>

<h2>📊 Visualizations</h2>
<ul>
  <li>✅ Call reasons distribution</li>
  <li>✅ Calls by day of week & month</li>
  <li>✅ Time series of calls over dates</li>
  <li>✅ Heatmaps: Day of week vs hour</li>
  <li>✅ Clustermaps: Temporal patterns</li>
</ul>

<h3>📷 Sample Plots</h3>
<table>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/df1078a2-568a-46fb-8cb4-77531f311b43" width="300"></td>
    <td><img src="https://github.com/user-attachments/assets/553bd8dd-8598-4f90-8e1c-52c86e7b134b" width="300"></td>
  </tr>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/8b90e24b-62d7-4ce9-bf7b-1561e1a921f1" width="300"></td>
    <td><img src="https://github.com/user-attachments/assets/2644a075-de16-4565-9635-10ade7a6fc7b" width="300"></td>
  </tr>
  <tr>
    <td colspan="2"><img src="https://github.com/user-attachments/assets/d03bc20e-390b-416b-a5c0-05662950ee18" width="300"></td>
  </tr>
</table>

<hr>

<h2>🚀 Future Work</h2>
<ul>
  <li>🌎 Add geographic maps using Plotly or Folium</li>
  <li>📊 Anomaly detection for unusual spikes</li>
  <li>🖥️ Interactive dashboard with <strong>Streamlit</strong> or <strong>Dash</strong></li>
</ul>

<hr>

<h2>🧪 How to Run</h2>

<pre>
# Clone this repository
git clone https://github.com/safikasi/911-Calls-Project.git

# Navigate to the folder
cd 911-Calls-Project

# Install dependencies
pip install pandas matplotlib seaborn numpy

# Run the analysis
python3 911_analysis.py
</pre>

<p>📌 <strong>Note:</strong> Ensure <code>911.csv</code> is in the same directory as your script.</p>

<hr>

<h2>📖 What I Learned</h2>
<ul>
  <li>✨ Advanced <code>pandas</code> functions: <code>.groupby()</code>, <code>.map()</code>, <code>.apply()</code></li>
  <li>📅 Time series handling with <code>datetime</code></li>
  <li>📊 Storytelling through visualizations</li>
  <li>🔥 Detecting patterns via heatmaps & pivots</li>
</ul>

<hr>

<h2>📜 Dataset Credit</h2>

<p>Dataset by <a href="https://www.kaggle.com/mchirico">Mike Chirico</a> on Kaggle.</p>
