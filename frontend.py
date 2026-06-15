import os
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide", page_title="MotoFix Pro")
st.title("MotoFix Pro-Hub")

# Pulls your Render URL from Streamlit Secrets
BACKEND_URL = "https://moto-backend-akei.onrender.com/api"

# Normal string, NO 'f' at the beginning
html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MotoFix Pro-Hub | Advanced Garage Management</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(6px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .animate-fade-in { animation: fadeIn 0.35s ease-out forwards; }
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
        
        <section class="max-w-7xl w-full mx-auto px-6 grid grid-cols-1 md:grid-cols-4 gap-4 pb-12 z-10 text-xs">
            <div class="bg-[#111726]/40 border border-slate-800/60 p-4 rounded-xl backdrop-blur-sm">
                <span class="text-xl">📦</span><h3 class="font-bold text-white mt-2 mb-1">Stock Ledger</h3><p class="text-slate-400 text-[11px]">Real-time item count auditing.</p>
            </div>
            <div class="bg-[#111726]/40 border border-slate-800/60 p-4 rounded-xl backdrop-blur-sm">
                <span class="text-xl">📊</span><h3 class="font-bold text-white mt-2 mb-1">Tuning Analytics</h3><p class="text-slate-400 text-[11px]">Calculate output gains with visual mapping.</p>
            </div>
            <div class="bg-[#111726]/40 border border-slate-800/60 p-4 rounded-xl backdrop-blur-sm">
                <span class="text-xl">📅</span><h3 class="font-bold text-white mt-2 mb-1">Booking</h3><p class="text-slate-400 text-[11px]">Secure upcoming physical workspace calendars.</p>
            </div>
            <div class="bg-[#111726]/40 border border-slate-800/60 p-4 rounded-xl backdrop-blur-sm">
                <span class="text-xl">🚨</span><h3 class="font-bold text-white mt-2 mb-1">Emergency SOS</h3><p class="text-slate-400 text-[11px]">Instantly track roadside dispatch operations.</p>
            </div>
        </section>
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

            <div id="sos-alert-box" class="hidden bg-[#1E1116] border border-red-500/30 rounded-2xl p-5 shadow-xl relative overflow-hidden animate-fade-in">
                <div class="absolute inset-y-0 left-0 w-1.5 bg-red-500"></div>
                <div class="flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
                    <div class="flex items-start gap-4">
                        <span class="text-3xl animate-bounce mt-1">🔧</span>
                        <div>
                            <h4 class="font-black text-red-400 uppercase tracking-wide text-xs">EMERGENCY RESPONDER MECHANIC EN-ROUTE</h4>
                            <p id="sos-status-text" class="text-xs text-slate-300 mt-1 leading-relaxed"></p>
                        </div>
                    </div>
                </div>
            </div>

            <div id="tab-stock" class="tab-content space-y-6">
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div class="bg-[#111726] border border-slate-800 p-5 rounded-2xl shadow-md">
                        <h5 class="text-[10px] font-bold uppercase tracking-wider text-slate-400 mb-0.5">On-Shelf Valuation</h5>
                        <p id="ui-valuation" class="text-3xl font-black text-emerald-400">₹0</p>
                    </div>
                    <div class="bg-[#111726] border border-slate-800 p-5 rounded-2xl shadow-md">
                        <h5 class="text-[10px] font-bold uppercase tracking-wider text-slate-400 mb-0.5">Items Below Safety Limit</h5>
                        <p id="ui-outages" class="text-3xl font-black text-amber-500">0 Spares Low</p>
                    </div>
                </div>

                <div class="bg-[#111726] border border-slate-800 p-5 rounded-2xl shadow-md">
                    <h3 class="text-xs font-black tracking-wider uppercase text-slate-300 mb-4 flex items-center gap-2">📥 Log New Spares Cargo Shipment</h3>
                    <form id="inventory-form" class="grid grid-cols-1 sm:grid-cols-3 lg:grid-cols-6 gap-3 items-end">
                        <input type="text" id="part-name" placeholder="Part Name" required class="w-full bg-[#0B0F19] border border-slate-800 rounded-xl px-3 py-2.5 text-xs text-white">
                        <input type="text" id="part-code" placeholder="Part Code" required class="w-full bg-[#0B0F19] border border-slate-800 rounded-xl px-3 py-2.5 text-xs text-white">
                        <input type="text" id="part-cat" placeholder="Category" required class="w-full bg-[#0B0F19] border border-slate-800 rounded-xl px-3 py-2.5 text-xs text-white">
                        <input type="number" id="part-price" placeholder="Cost Price (₹)" required class="w-full bg-[#0B0F19] border border-slate-800 rounded-xl px-3 py-2.5 text-xs text-white">
                        <input type="number" id="part-alert-limit" placeholder="Alert Limit (Default: 3)" class="w-full bg-[#0B0F19] border border-slate-800 rounded-xl px-3 py-2.5 text-xs text-white">
                        <div class="flex gap-2">
                            <input type="number" id="part-qty" placeholder="Qty" required class="w-full bg-[#0B0F19] border border-slate-800 rounded-xl px-3 py-2.5 text-xs text-white">
                            <button type="button" onclick="submitInventory()" class="w-full bg-cyan-500 hover:bg-cyan-400 text-slate-950 font-black text-[10px] uppercase tracking-wider px-4 py-2.5 rounded-xl transition">Add To Shelf</button>
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
                                    <th class="p-3.5 text-center">Quantity Tracker</th>
                                    <th class="p-3.5 text-right">Actions</th>
                                </tr>
                            </thead>
                            <tbody id="ledger-table-body" class="divide-y divide-slate-800/40"></tbody>
                        </table>
                    </div>
                </div>
            </div>

            <div id="tab-analytics" class="tab-content hidden max-w-2xl mx-auto bg-[#111726] border border-slate-800 p-6 rounded-2xl shadow-xl space-y-6">
                <div><h2 class="text-sm font-black uppercase tracking-wider text-white border-b border-slate-800 pb-3">Vehicle Diagnostic Overhaul Metrics</h2></div>
                <div class="space-y-4 text-xs">
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                        <div><label class="block text-slate-400 font-medium mb-1">Baseline Factory Output (BHP)</label><input type="number" id="metric-pre" value="120" class="w-full bg-[#0B0F19] border border-slate-800 rounded-xl px-3 py-2.5 text-white font-mono"></div>
                        <div><label class="block text-slate-400 font-medium mb-1">Post-Tune Target (BHP)</label><input type="number" id="metric-post" value="175" class="w-full bg-[#0B0F19] border border-slate-800 rounded-xl px-3 py-2.5 text-white font-mono"></div>
                    </div>
                    <button type="button" onclick="evaluatePerformanceTuning()" class="w-full bg-cyan-500 hover:bg-cyan-400 text-slate-950 font-bold py-2.5 rounded-xl transition text-xs uppercase tracking-wider">Run Evaluation Logic</button>
                </div>
                <div id="analysis-visual-chart" class="hidden bg-[#0B0F19] border border-slate-800 p-4 rounded-xl space-y-4">
                    <div class="space-y-3">
                        <div>
                            <div class="flex justify-between text-[10px] mb-1"><span class="text-slate-400">Baseline Level</span><span id="txt-pre-val" class="font-mono text-white">120</span></div>
                            <div class="w-full bg-slate-900 h-3 rounded-full overflow-hidden border border-slate-800"><div id="bar-pre-val" class="bg-slate-500 h-full rounded-full transition-all duration-700" style="width: 0%"></div></div>
                        </div>
                        <div>
                            <div class="flex justify-between text-[10px] mb-1"><span class="text-cyan-400 font-bold">Post-Overhaul Compression Map</span><span id="txt-post-val" class="font-mono text-cyan-400 font-bold">175</span></div>
                            <div class="w-full bg-slate-900 h-3 rounded-full overflow-hidden border border-slate-800"><div id="bar-post-val" class="bg-gradient-to-r from-cyan-500 to-blue-500 h-full rounded-full transition-all duration-700" style="width: 0%"></div></div>
                        </div>
                    </div>
                    <div class="p-2.5 bg-cyan-950/20 border border-cyan-800/40 rounded-lg text-center"><p id="evaluation-verdict" class="text-[11px] font-semibold text-cyan-300"></p></div>
                </div>
            </div>

            <div id="tab-book" class="tab-content hidden max-w-xl mx-auto bg-[#111726] border border-slate-800 p-6 rounded-2xl shadow-xl space-y-6">
                <h2 class="text-sm font-black uppercase tracking-wider text-white border-b border-slate-800 pb-3 text-center">Advanced Booking Block</h2>
                <form id="booking-form" class="space-y-3.5 text-xs">
                    <input type="text" id="book-name" placeholder="Owner Full Name" required class="w-full bg-[#0B0F19] border border-slate-800 rounded-xl px-3 py-2.5 text-white">
                    <input type="text" id="book-plate" placeholder="Vehicle License Plate Number" required class="w-full bg-[#0B0F19] border border-slate-800 rounded-xl px-3 py-2.5 text-white font-mono uppercase">
                    <select id="book-type" class="w-full bg-[#0B0F19] border border-slate-800 rounded-xl px-3 py-2.5 text-white">
                        <option value="Full Engine Blueprint Tuning">Full Engine Blueprint Tuning</option>
                        <option value="Performance Brake Calibration">Performance Brake Calibration</option>
                        <option value="Electrical Matrix Rewire">Electrical Matrix Rewire</option>
                    </select>
                    <div class="grid grid-cols-2 gap-2">
                        <input type="date" id="book-date" required class="bg-[#0B0F19] border border-slate-800 rounded-xl px-3 py-2.5 text-white">
                        <input type="time" id="book-time" required class="bg-[#0B0F19] border border-slate-800 rounded-xl px-3 py-2.5 text-white">
                    </div>
                    <button type="button" onclick="submitBooking()" class="w-full bg-cyan-500 hover:bg-cyan-400 text-slate-950 font-black py-2.5 rounded-xl transition text-xs uppercase tracking-wider">Confirm Appointment</button>
                </form>

                <div id="ui-booking-box" class="hidden space-y-2 pt-2 border-t border-slate-800">
                    <h4 class="text-[10px] font-bold uppercase tracking-widest text-slate-400">Active Booked Workshop Slates</h4>
                    <div id="ui-booking-list" class="space-y-2"></div>
                </div>
            </div>

            <div id="tab-essentials" class="tab-content hidden space-y-6">
                <div class="border-b border-slate-800 pb-2">
                    <h2 class="text-sm font-black uppercase tracking-wider text-white">Essential On-Road Toolsets</h2>
                </div>
                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5">
                    <div class="bg-[#111726] border border-slate-800 rounded-2xl overflow-hidden shadow-md p-4 flex flex-col justify-between space-y-4">
                        <div>
                            <h4 class="font-bold text-sm text-white">Microfiber Cleaning Combo Pack</h4>
                            <p class="text-[11px] text-slate-400 mt-1">Super absorbent lint-free wash towels.</p>
                        </div>
                        <div class="flex items-center justify-between border-t border-slate-800/60 pt-3">
                            <span class="font-black text-cyan-400 text-sm">₹450</span>
                            <button type="button" onclick="pushToShelf('Microfiber Cleaning Combo Pack', 450)" class="bg-cyan-500 hover:bg-cyan-400 text-slate-950 text-[10px] uppercase font-black tracking-wider px-4 py-2 rounded-xl transition">Purchase</button>
                        </div>
                    </div>
                    <div class="bg-[#111726] border border-slate-800 rounded-2xl overflow-hidden shadow-md p-4 flex flex-col justify-between space-y-4">
                        <div>
                            <h4 class="font-bold text-sm text-white">Heavy-Duty Screw & Plier Toolkit</h4>
                            <p class="text-[11px] text-slate-400 mt-1">Chrome-vanadium steel multi-size tools.</p>
                        </div>
                        <div class="flex items-center justify-between border-t border-slate-800/60 pt-3">
                            <span class="font-black text-cyan-400 text-sm">₹1250</span>
                            <button type="button" onclick="pushToShelf('Heavy-Duty Screw & Plier Toolkit', 1250)" class="bg-cyan-500 hover:bg-cyan-400 text-slate-950 text-[10px] uppercase font-black tracking-wider px-4 py-2 rounded-xl transition">Purchase</button>
                        </div>
                    </div>
                </div>
            </div>

        </main>
    </div>

    <script>
    const BACKEND_URL = "PYTHON_WILL_REPLACE_THIS";

    function switchTab(tabId){
        document.querySelectorAll('.tab-content').forEach(tab => tab.classList.add('hidden'));
        document.getElementById(tabId).classList.remove('hidden');
        document.querySelectorAll('[id^="btn-tab"]').forEach(btn => {
            btn.classList.remove('bg-cyan-500', 'text-slate-950', 'shadow-md');
            btn.classList.add('text-slate-400');
        });
        const activeBtn = document.getElementById('btn-' + tabId);
        if(activeBtn) {
            activeBtn.classList.add('bg-cyan-500', 'text-slate-950', 'shadow-md');
        }
    }

    function enterAppConsole() {
        document.getElementById('landing-page-view').classList.add('hidden');
        document.getElementById('main-app-dashboard-view').classList.remove('hidden');
        syncStateWithPostgres();
        loadBookings();
    }

    async function syncStateWithPostgres() {
        try {
            const res = await fetch(`${BACKEND_URL}/inventory`);
            if (!res.ok) return;
            const allData = await res.json();
            populateLedgerTable(allData);
            let total=0, low=0;
            allData.forEach(i=>{
                total += (i.cost_price||0)*(i.available_units||0);
                if((i.available_units||0) <= (i.alert_limit||3)) low++;
            });
            document.getElementById('ui-valuation').innerText='₹'+total;
            document.getElementById('ui-outages').innerText=low+' Spares Low';
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
                <td class="p-3.5 text-center font-bold text-amber-500 font-mono">${item.alert_limit || 3}</td>
                <td class="p-3.5 text-center">
                    <div class="flex items-center justify-center gap-2">
                        <button onclick="updateQty('${item.part_code}', -1)" class="bg-slate-700 hover:bg-red-600 text-white w-6 h-6 rounded font-bold">-</button>
                        <span class="w-8 text-center font-black">${item.available_units}</span>
                        <button onclick="updateQty('${item.part_code}', 1)" class="bg-slate-700 hover:bg-emerald-600 text-white w-6 h-6 rounded font-bold">+</button>
                    </div>
                </td>
                <td class="p-3.5 text-right space-x-3">
                    <button onclick="deletePart('${item.part_code}')" class="text-rose-500 hover:text-rose-400 text-[10px] uppercase font-extrabold">Delete</button>
                </td>
            </tr>
        `).join('');
    }

    async function submitInventory() {
        const nameEl = document.getElementById('part-name').value;
        const codeEl = document.getElementById('part-code').value;

        // 1. Prevent blank submissions
        if(!nameEl || !codeEl) {
            alert("⚠️ Please fill out at least the Part Name and Part Code!");
            return;
        }

        const payload = {
            part_name: nameEl,
            part_code: codeEl,
            category: document.getElementById('part-cat').value || 'Uncategorized',
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
                alert("✅ Part added to shelf successfully!");
                syncStateWithPostgres();
            } else {
                // 2. Catch Database rule violations
                alert("❌ Failed to add part. Ensure the Part Code is completely unique and not already in the ledger.");
            }
        } catch (err) {
            // 3. Catch Render wake-up delays
            alert("⏳ Network error: The database server might be waking up from sleep. Wait 30 seconds and try clicking Add again.");
        }
    }

    async function updateQty(code, change) {
        try {
            const response = await fetch(`${BACKEND_URL}/inventory/update-qty`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ part_code: code, change: change })
            });
            if (response.ok) syncStateWithPostgres();
        } catch (err) { console.error(err); }
    }

    async function submitBooking() {
        const payload = {
            name: document.getElementById('book-name').value,
            plate: document.getElementById('book-plate').value,
            type: document.getElementById('book-type').value,
            date: document.getElementById('book-date').value,
            time: document.getElementById('book-time').value
        };
        try {
            const res = await fetch(`${BACKEND_URL}/bookings`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(payload)
            });
            if(res.ok) {
                document.getElementById('booking-form').reset();
                alert("Appointment locked!");   
                loadBookings(); 
            }
        } catch (err) { console.error(err); }
    }

    async function loadBookings() {
        try {
            const res = await fetch(`${BACKEND_URL}/bookings`);
            const bookings = await res.json();
            const listContainer = document.getElementById('ui-booking-list');
            const boxContainer = document.getElementById('ui-booking-box');
            listContainer.innerHTML = ''; 
            if (bookings.length > 0) {
                boxContainer.classList.remove('hidden');
                bookings.forEach((booking) => {
                    listContainer.innerHTML += `
                        <div class="bg-[#0B0F19] border border-slate-800 rounded-xl p-3 flex justify-between items-center text-[11px] text-slate-300">
                            <div><strong class="text-white">${booking.name}</strong> • ${booking.plate}<br><span class="text-cyan-500">${booking.date} @ ${booking.time}</span></div>
                            <button onclick="deleteAppointment(${booking.id})" class="text-red-400 font-bold ml-2">DELETE</button>
                        </div>
                    `;
                });
            } else { boxContainer.classList.add('hidden'); }
        } catch (err) { console.error(err); }
    }

    async function deleteAppointment(id) {
        try {
            const res = await fetch(`${BACKEND_URL}/bookings/${id}`, { method: 'DELETE' });
            if (res.ok) loadBookings();
        } catch (err) { console.error(err); }
    }

    async function pushToShelf(partName, price) {
        const data = { part_name: partName, part_code: 'KIT-' + Math.floor(Math.random() * 1000), category: 'Essentials', cost_price: price, available_units: 1, alert_limit: 3 };
        try {
            const response = await fetch(`${BACKEND_URL}/inventory`, {
                method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data)
            });
            if (response.ok) { alert("Added!"); syncStateWithPostgres(); }
        } catch (err) { console.error(err); }
    }

    function evaluatePerformanceTuning() {
        const preVal = parseFloat(document.getElementById('metric-pre').value) || 0;
        const postVal = parseFloat(document.getElementById('metric-post').value) || 0;
        if (preVal === 0 || postVal === 0) return;
        document.getElementById('analysis-visual-chart').classList.remove('hidden');
        document.getElementById('txt-pre-val').innerText = `${preVal} BHP`;
        document.getElementById('txt-post-val').innerText = `${postVal} BHP`;
        const maxRef = Math.max(preVal, postVal, 200);
        setTimeout(() => {
            document.getElementById('bar-pre-val').style.width = `${(preVal / maxRef) * 100}%`;
            document.getElementById('bar-post-val').style.width = `${(postVal / maxRef) * 100}%`;
        }, 100);
        const gain = (((postVal - preVal) / preVal) * 100).toFixed(1);
        document.getElementById('evaluation-verdict').innerHTML = `📈 Evaluation Matrix Complete: Tuning map gained <strong class="text-white font-bold">+${gain}%</strong>!`;
    }

    async function triggerEmergencySOS() {
        document.getElementById('sos-alert-box').classList.remove('hidden');
        document.getElementById('sos-status-text').innerHTML = `Alert logged! Dispatching technician <strong class="text-white">Vikram Rathore</strong> directly.<br><span class="text-cyan-400 font-bold">🚨 ETA: 20 mins</span>`;
    }

    document.addEventListener('DOMContentLoaded', () => {
        syncStateWithPostgres();
        loadBookings();
    });

    async function deletePart(code) {
    if (!confirm("Delete this part?")) return;

    try {
        const response = await fetch(`${BACKEND_URL}/inventory/delete`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                part_code: code
            })
        });

        if (response.ok) {
            alert("Part deleted successfully!");
            syncStateWithPostgres();
        } else {
            alert("Failed to delete part.");
        }
    } catch (err) {
        console.error(err);
        alert("Network error while deleting.");
    }
}
    </script>
</body>
</html>"""

# THIS IS THE CRITICAL LINE THAT MAKES YOUR BUTTONS WORK!
final_html = html.replace("PYTHON_WILL_REPLACE_THIS", BACKEND_URL)

components.html(final_html, height=1000, scrolling=True)
