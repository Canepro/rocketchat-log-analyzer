# 🐛 Release Notes: v2.1.4 - "Chart Filtering Bug Fix" Release

## 🎯 **What's Fixed in v2.1.4**

### 🐛 **Critical Bug Fixes**
- **🖱️ Chart Click-to-Filter Functionality**: Fixed broken chart filtering that was redirecting to logs but showing "0 found" results
  - Resolved DataTable initialization and filtering reference mismatches
  - Fixed inconsistent table references between `$('table.display').DataTable()` and filtering functions
  - Implemented global DataTable instance management with `window.logsDataTable`
- **🔍 Search Compatibility**: Switched from column-specific search to global search for better reliability
  - Improved date format compatibility and filtering logic
  - Enhanced search functionality across all log data
- **⚡ Race Condition Prevention**: Added proper async handling and increased timeout from 500ms to 1000ms
  - Better error handling for DataTable initialization timing
  - Improved reliability of chart-to-table interactions

### 🔧 **Technical Improvements**
- **📊 DataTable Management**: Consistent DataTable instance handling across all interactive features
- **🛡️ Enhanced Error Handling**: Better timeout handling and error reporting for user interactions
- **🔄 Code Quality**: Clean implementation following proper GitHub issue tracking workflow

### 🎯 **User Experience Improvements**
- **✅ Seamless Chart Filtering**: Chart click-to-filter functionality now works correctly and reliably
- **📈 Better Performance**: Improved responsiveness of interactive dashboard features
- **🔧 Debugging Support**: Enhanced error reporting for troubleshooting interactive features

---

## 🛠️ **Technical Details**

### **Files Modified**
- `templates/report_template.html`: Fixed DataTable initialization and filtering logic
- `config.py`: Updated version to 2.1.4
- `CHANGELOG.md`: Added comprehensive v2.1.4 changelog entry

### **Root Cause Analysis**
The chart filtering bug was caused by inconsistent DataTable references:
- **Initialization**: Using `$('table.display').DataTable()` 
- **Filtering Functions**: Attempting to access different table instances
- **Solution**: Implemented global `window.logsDataTable` instance for consistent access

### **Testing Verification**
- ✅ All 7 unit tests passing
- ✅ Interactive chart filtering working correctly
- ✅ DataTable integration functioning properly
- ✅ Container deployment successful

---

## 🚀 **Upgrade Instructions**

### **From v2.1.3 to v2.1.4**
This is a **patch release** containing critical bug fixes. Upgrade is recommended for all users.

**Docker/Podman Users:**
```bash
# Pull the latest image
podman pull ghcr.io/canepro/rocketchat-log-analyzer:v2.1.4
```

**Manual Installation:**
```bash
git pull origin main
# No dependency changes required
```

---

## 🎉 **What's Next**

v2.1.4 completes the interactive dashboard functionality with all chart filtering features working correctly. Future releases will focus on:

- Advanced analytics and reporting features
- Enhanced log pattern recognition
- Performance optimizations for large datasets
- Additional export formats and integrations

For detailed development plans, see [`ROADMAP.md`](ROADMAP.md).

---

**Release Date:** August 1, 2025  
**Release Type:** Patch Release (Bug Fix)  
**Compatibility:** Full backward compatibility with v2.1.x configurations
