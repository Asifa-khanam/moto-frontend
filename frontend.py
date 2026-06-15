import os
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide", page_title="MotoFix Pro")
st.title("MotoFix Pro-Hub")

# IMPORTANT: During local testing, this will default to localhost. 
# When you deploy, add BACKEND_API_URL as an environment variable in Streamlit Cloud.
BACKEND_URL = os.environ.get("BACKEND_API_URL", "http://localhost:5000/api")

html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MotoFix Pro-Hub</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(6px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        .animate-fade-in {{ animation: fadeIn 0.35s ease-out forwards; }}
    </style>
</head>
<body class="bg-[#0B0F19] text-slate-100 min-h-screen font-sans antialiased">

    <div id="landing-page-view" class="min-h-screen flex flex-col justify-between relative overflow-hidden">
        <div class="absolute top-[-10%] left-[-10%] w-[500px] h-[500px] bg-cyan-500/10 rounded-full blur-[120px] pointer-events-none"></div>
        <div class="absolute bottom-[-10%] right-[-10%] w-[500px] h-[500px] bg-blue-600/10 rounded-full blur-[120px] pointer-events-none"></div>

        <header class="max-w-7xl w-full mx-auto px-6 py-5 flex justify-between items-center z-10">
            <div class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-cyan-500 to-blue-600 flex items-center justify-center font-black text-xl text-slate-900 shadow-lg shadow-cyan-500/20">M</div>
                <span class="text-lg font-black tracking-wider text-white">MOTOFIX PRO</span>
            </div>
            <button onclick="enterAppConsole()" class="border border-slate-700 hover:border-cyan-500 text-slate-300 hover:text-cyan-400 font-bold text-xs uppercase tracking-wider px-4 py-2 rounded-xl transition">Launch Hub</button>
        </header>

        <main class="max-w-5xl mx-auto px-6 text-center py-12 md:py-20 z-10 my-auto space-y-8 animate-fade-in">
            <h1 class="text-4xl md:text-6xl font-black tracking-tight text-white leading-tight">Streamline Workshop Operations <br><span class="bg-clip-text text-transparent bg-gradient-to-r from-cyan-400 via-blue-500 to-indigo-500">With Digital Telemetry Control</span></h1>
            <p class="text-sm md:text-base text-slate-400 max-w-2xl mx-auto leading-relaxed">Track precision warehouse parts inventory, manage client engine parts, run live dyno performance, analytics simulations and access immediate emergency roadside dispatch logic.</p>
            <div class="pt-4">
                <button onclick="enterAppConsole()" class="bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-400 hover:to-blue-500 text-slate-950 font-black text-xs uppercase tracking-widest px-8 py-4 rounded-xl shadow-lg shadow-cyan-500/20 transition transform hover:-translate-y-0.5">Enter Management Console 🚀</button>
            </div>
        </main>
    </div>

    <div id="main-app-dashboard-view" class="hidden">
        <main class="max-w-7xl w-full mx-auto p-3 md:p-6 space-y-6">
            <header class="bg-[#161F30] border border-slate-800 rounded-2xl p-4 flex flex-col lg:flex-row justify-between items-start lg:items-center gap-4 shadow-xl">
                <div class="flex items-center gap-3">
                    <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-cyan-500 to-blue-600 flex items-center justify-center font-black text-xl text-slate-900 shadow-lg shadow-cyan-500/20">M</div>
                    <div>
                        <h1 class="text-xl font-black tracking-wider text-white">MOTOFIX PRO-HUB</h1>
                        <p class="text-[10px] text-cyan-400 font-bold uppercase tracking-widest">PostgreSQL Connected</p>
                    </div>
                </div>
                <div class="flex flex-wrap gap-1.5 w-full lg:w-auto">
                    <button type="button" onclick="switchTab('tab-stock')" id="btn-tab-stock" class="flex-1 sm:flex-initial text-xs uppercase font-extrabold tracking-wider px-4 py-2.5 rounded-xl transition bg-cyan-500 text-slate-950 shadow-md">📦 Stock Ledger</button>
                    <button type="button" onclick="switchTab('tab-analytics')" id="btn-tab-analytics" class="flex-1 sm:flex-initial text-xs uppercase font-extrabold tracking-wider px-4 py-2.5 rounded-xl transition text-slate-400 hover:bg-slate-800/40">📊 Service Analytics</button>
                    <button type="button" onclick="switchTab('tab-book')" id="btn-tab-book" class="flex-1 sm:flex-initial text-xs uppercase font-extrabold tracking-wider px-4 py-2.5 rounded-xl transition text-slate-400 hover:bg-slate-800/40">📅 Book Appointment</button>
                    <button type="button" onclick="switchTab('tab-essentials')" id="btn-tab-essentials" class="flex-1 sm:flex-initial text-xs uppercase font-extrabold tracking-wider px-4 py-2.5 rounded-xl transition text-slate-400 hover:bg-slate-800/40">🛍 Essentials Shop</button>
                    <button type="button" onclick="triggerEmergencySOS()" class="w-full sm:w-auto bg-gradient-to-r from-red-600 to-rose-600 text-white text-xs font-black tracking-wider px-5 py-2.5 rounded-xl transition shadow-lg shadow-red-900/30">🚨 SOS BREAKDOWN</button>
                </div>
            </header>

            <div id="tab-stock" class="tab-content space-y-6">
                <div class="bg-[#111726] border border-slate-800 p-5 rounded-2xl shadow-md">
                    <h3 class="text-xs font-black tracking-wider uppercase text-slate-300 mb-4 flex items-center gap-2">📥 Log New Spares Cargo Shipment</h3>
                    <form id="inventory-form" class="grid grid-cols-1 sm:grid-cols-3 lg:grid-cols-6 gap-3 items-end">
                        <input type="text" id="part-name" placeholder="Part Name" required class="w-full bg-[#0B0F19] border border-slate-800 rounded-xl px-3 py-2.5 text-xs text-white focus:outline-none focus:border-cyan-500">
                        <input type="text" id="part-code" placeholder="Part Code" required class="w-full bg-[#0B0F19] border border-slate-800 rounded-xl px-3 py-2.5 text-xs text-white focus:outline-none focus:border-cyan-500">
                        <input type="text" id="part-cat" placeholder="Category" required class="w-full bg-[#0B0F19] border border-slate-800 rounded-xl px-3 py-2.5 text-xs text-white focus:outline-none focus:border-cyan-500">
                        <input type="number" id="part-price" placeholder="Cost Price (₹)" required class="w-full bg-[#0B0F19] border border-slate-800 rounded-xl px-3 py-2.5 text-xs text-white focus:outline-none focus:border-cyan-500">
                        <input type="number" id="part-alert-limit" placeholder="Alert Limit" class="w-full bg-[#0B0F19] border border-slate-800 rounded-xl px-3 py-2.5 text-xs text-white focus:outline-none focus:border-cyan-500">
                        <div class="flex gap-2">
                            <input type="number" id="part-qty" placeholder="Qty" required class="w-full bg-[#0B0F19] border border-slate-800 rounded-xl px-3 py-2.5 text-xs text-white focus:outline-none focus:border-cyan-500">
                            <button type="button" onclick="submitInventory()" class="w-full bg-cyan-500 hover:bg-cyan-400 text-slate-950 font-black text-[10px] uppercase tracking-wider px-4 py-2.5 rounded-xl transition">Add</button>
                        </div>
                    </form>
                </div>
                
                <div class="bg-[#111726] border border-slate-800 rounded-2xl shadow-md overflow-hidden">
                    <div class="p-4 border-b border-slate-800 bg-[#161F30]"><h3 class="text-xs font-black tracking-wider uppercase text-white">Live Spares Count Ledger</h3></div>
                    <div class="overflow-x-auto">
                        <table class="w-full text-left text-xs">
                            <thead>
                                <tr class="bg-[#0D1321] text-slate-400 font-bold border-b border-slate-800 uppercase tracking-wider text-[10px]">
                                    <th class="p-3.5">Part Details</th>
                                    <th class="p-3.5">Category</th>
                                    <th class="p-3.5">Unit Price</th>
                                    <th class="p-3.5 text-center">Alert Limit</th>
                                    <th class="p-3.5 text-center">Quantity</th>
                                    <th class="p-3.5 text-right">Actions</th>
                                </tr>
                            </thead>
                            <tbody id="ledger-table-body" class="divide-y divide-slate-800/40"></tbody>
                        </table>
                    </div>
                </div>
            </div>

            <div id="tab-analytics" class="tab-content hidden">
                <p class="text-slate-400 text-sm">Analytics dashboard placeholder.</p>
            </div>
            
            <div id="tab-book" class="tab-content hidden">
                <p class="text-slate-400 text-sm">Booking dashboard placeholder.</p>
            </div>
            
            <div id="tab-essentials" class="tab-content hidden">
                 <p class="text-slate-400 text-sm">Shop dashboard placeholder.</p>
            </div>
        </main>
    </div>

    <script>
    // Dynamically inject the API URL defined in Streamlit
    const BACKEND_URL = "PYTHON_WILL_REPLACE_THIS";

    function switchTab(tabId){
        // Hide all tabs
        document.querySelectorAll('.tab-content').forEach(tab => tab.classList.add('hidden'));
        
        // Show the selected tab
        document.getElementById(tabId).classList.remove('hidden');
        
        // Reset all buttons 
        document.querySelectorAll('[id^="btn-tab"]').forEach(btn => {
            btn.classList.remove('bg-cyan-500', 'text-slate-950', 'shadow-md');
            btn.classList.add('text-slate-400');
        });
        
        // Highlight the clicked button
        const activeBtn = document.getElementById('btn-' + tabId);
        if(activeBtn) {
            activeBtn.classList.add('bg-cyan-500', 'text-slate-950', 'shadow-md');
        }
    }

    function enterAppConsole() {
        document.getElementById('landing-page-view').classList.add('hidden');
        document.getElementById('main-app-dashboard-view').classList.remove('hidden');
        syncStateWithPostgres();
    }

    async function syncStateWithPostgres() {
        try {
            const res = await fetch(`${BACKEND_URL}/inventory`);
            if (!res.ok) return console.error("Database connection failed");
            const allData = await res.json();
            populateLedgerTable(allData);
        } catch (err) { 
            console.error("Network error:", err); 
        }
    }

    function populateLedgerTable(items) {
        const tbody = document.getElementById('ledger-table-body');
        tbody.innerHTML = items.map(item => `
            <tr class="hover:bg-slate-800/10 transition">
                <td class="p-3.5 font-bold text-slate-200">${item.part_name}<br><span class="text-[10px] text-slate-500 font-mono">${item.part_code}</span></td>
                <td class="p-3.5 text-slate-400 font-medium">${item.category}</td>
                <td class="p-3.5 font-semibold text-slate-300">₹${item.cost_price}</td>
                <td class="p-3.5 text-center font-bold text-amber-500 font-mono">${item.alert_limit}</td>
                <td class="p-3.5 text-center font-black">${item.available_units}</td>
                <td class="p-3.5 text-right space-x-3">
                    <button onclick="deletePart('${item.part_code}')" class="text-rose-500 hover:text-rose-400 text-[10px] uppercase font-extrabold">Delete</button>
                </td>
            </tr>
        `).join('');
    }

    async function submitInventory() {
        const payload = {
            part_name: document.getElementById('part-name').value,
            part_code: document.getElementById('part-code').value,
            category: document.getElementById('part-cat').value,
            cost_price: parseFloat(document.getElementById('part-price').value) || 0,
            available_units: parseInt(document.getElementById('part-qty').value) || 0,
            alert_limit: parseInt(document.getElementById('part-alert-limit').value) || 3
        };
        try {
            const response = await fetch(`${BACKEND_URL}/inventory`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(payload)
            });
            if(response.ok) {
                document.getElementById('inventory-form').reset();
                syncStateWithPostgres();
            }
        } catch (err) { 
            alert("Network error connecting to Flask backend."); 
        }
    }

    async function deletePart(code) {
        if (!confirm(`Delete part code [${code}]?`)) return;
        await fetch(`${BACKEND_URL}/inventory/delete`, {
            method: 'POST', 
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ part_code: code })
        });
        syncStateWithPostgres();
    }
    </script>
</body>
</html>"""

# Streamlit Component Rendering
components.html(html, height=1000, scrolling=True)
