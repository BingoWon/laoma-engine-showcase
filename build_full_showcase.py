import os, glob

OUTPUT_FILE = "/Users/bingo/Code/LYi/projects/laoma-engine-showcase/index.html"
assets_dir = "/Users/bingo/Code/LYi/projects/laoma-engine-showcase/assets"

# Read existing generate_ultimate_canvas.py
with open("/Users/bingo/Code/LYi/projects/laoma-engine-showcase/generate_ultimate_canvas.py") as f:
    code = f.read()

# 1. Fix screens paths: replace ./assets/screens/screen_01_idle.png etc with real screenshots
screen_map = [
    ("screen_01_idle.png", "Screenshot_20260919_174540_com_lyi_laomayoyo_MainActivity.JPG"),
    ("screen_02_interaction.png", "Screenshot_20260919_174600_com_lyi_laomayoyo_MainActivity.JPG"),
    ("screen_03_dirty.png", "Screenshot_20260919_174613_com_lyi_laomayoyo_MainActivity.JPG"),
    ("screen_04_cleaning.png", "Screenshot_20260919_174628_com_lyi_laomayoyo_MainActivity.JPG"),
    ("screen_05_feeding.png", "Screenshot_20260919_174648_com_lyi_laomayoyo_MainActivity.JPG"),
    ("screen_06_playing.png", "Screenshot_20260919_174700_com_lyi_laomayoyo_MainActivity.JPG"),
    ("screen_07_medical.png", "Screenshot_20260919_174713_com_lyi_laomayoyo_MainActivity.JPG"),
    ("screen_08_night.png", "Screenshot_20260919_174724_com_lyi_laomayoyo_MainActivity.JPG"),
]
for old_s, new_s in screen_map:
    code = code.replace(f"./assets/screens/{old_s}", f"./assets/screenshots/{new_s}")

# 2. Add avatar_imyrs to TEAM_MEMBERS
old_team = """      { name: 'Lex', alias: 'Lex', role: '数据服务架构', avatar: './assets/app_assets/avatars/avatar_lex.png', desc: '端侧 IndexedDB 双写持久化机制、数据加密与离线状态恢复。' }
    ];"""

new_team = """      { name: 'Lex', alias: 'Lex', role: '数据服务架构', avatar: './assets/app_assets/avatars/avatar_lex.png', desc: '端侧 IndexedDB 双写持久化机制、数据加密与离线状态恢复。' },
      { name: '易明', alias: 'imyrs', role: '视觉算法系统', avatar: './assets/app_assets/avatars/avatar_imyrs.png', desc: '端侧视觉特征提取、图像比例矫正与零剪裁自适应渲染管线。' }
    ];"""
code = code.replace(old_team, new_team)

# Update zone-team subtitle
code = code.replace("14 位工程贡献者与系统总线节点网格", "15 位工程贡献者与系统总线节点网格")
code = code.replace("14 REAL CONTRIBUTORS", "15 REAL CONTRIBUTORS")
code = code.replace("14 MODULE OWNERS", "15 MODULE OWNERS")
code = code.replace("grid-cols-7 gap-4", "grid-cols-5 gap-4")

# 3. In zone-candidates: Add office_dirty_cat_candidate_1..3 and home_cat_bg_clean/dirty/touch
candidates_insert_anchor = """        <!-- Section C: Scenic Bento & Layout Explorations -->"""
candidates_new_section = """        <!-- Section B.2: Office Ambient Dirty Cat Candidates & Mid-Res Touch Samples -->
        <div class="mb-5">
          <div class="flex items-center justify-between mb-2">
            <span class="text-xs font-black text-slate-700 font-mono flex items-center gap-1.5">
              <span class="w-2 h-2 rounded-full bg-amber-500"></span>
              <span>GROUP B.2 · 办公环境光照脏污候选与中分辨率手势验证样张 (851×1848 / 650×1414 · 零剪裁)</span>
            </span>
            <span class="text-[10px] font-mono text-slate-400">6 SAMPLES · NATIVE RATIO</span>
          </div>
          <div class="grid grid-cols-6 gap-3">
            <div class="bg-slate-50 p-2 rounded-2xl border border-slate-200 cursor-pointer hover:border-amber-400 transition-all" onclick="inspectImage('./assets/candidates/office_dirty_cat_candidate_1.png', '办公光照候选 01 · 自然漫反射工况 (851×1848)')">
              <div class="w-full aspect-phone bg-slate-900/5 rounded-xl overflow-hidden mb-1 flex items-center justify-center">
                <img src="./assets/candidates/office_dirty_cat_candidate_1.png" class="no-crop-img" alt="办公候选1">
              </div>
              <div class="text-[9px] font-bold text-slate-700 font-mono truncate">OFFICE_DIRTY_01</div>
              <div class="text-[8px] text-slate-400 font-mono">851×1848 (0.460)</div>
            </div>
            <div class="bg-slate-50 p-2 rounded-2xl border border-slate-200 cursor-pointer hover:border-amber-400 transition-all" onclick="inspectImage('./assets/candidates/office_dirty_cat_candidate_2.png', '办公光照候选 02 · 顶棚荧光灯工况 (851×1848)')">
              <div class="w-full aspect-phone bg-slate-900/5 rounded-xl overflow-hidden mb-1 flex items-center justify-center">
                <img src="./assets/candidates/office_dirty_cat_candidate_2.png" class="no-crop-img" alt="办公候选2">
              </div>
              <div class="text-[9px] font-bold text-slate-700 font-mono truncate">OFFICE_DIRTY_02</div>
              <div class="text-[8px] text-slate-400 font-mono">851×1848 (0.460)</div>
            </div>
            <div class="bg-slate-50 p-2 rounded-2xl border border-slate-200 cursor-pointer hover:border-amber-400 transition-all" onclick="inspectImage('./assets/candidates/office_dirty_cat_candidate_3.png', '办公光照候选 03 · 阴影背光测试工况 (851×1848)')">
              <div class="w-full aspect-phone bg-slate-900/5 rounded-xl overflow-hidden mb-1 flex items-center justify-center">
                <img src="./assets/candidates/office_dirty_cat_candidate_3.png" class="no-crop-img" alt="办公候选3">
              </div>
              <div class="text-[9px] font-bold text-slate-700 font-mono truncate">OFFICE_DIRTY_03</div>
              <div class="text-[8px] text-slate-400 font-mono">851×1848 (0.460)</div>
            </div>
            <div class="bg-slate-50 p-2 rounded-2xl border border-slate-200 cursor-pointer hover:border-amber-400 transition-all" onclick="inspectImage('./assets/candidates/home_cat_bg_clean.png', '中分辨率工况 · 851×1849 常态居室猫咪')">
              <div class="w-full aspect-phone bg-slate-900/5 rounded-xl overflow-hidden mb-1 flex items-center justify-center">
                <img src="./assets/candidates/home_cat_bg_clean.png" class="no-crop-img" alt="中模常态">
              </div>
              <div class="text-[9px] font-bold text-slate-700 font-mono truncate">CAT_CLEAN_MID</div>
              <div class="text-[8px] text-slate-400 font-mono">851×1849 (0.460)</div>
            </div>
            <div class="bg-slate-50 p-2 rounded-2xl border border-slate-200 cursor-pointer hover:border-amber-400 transition-all" onclick="inspectImage('./assets/candidates/home_cat_dirty_tap.png', '中分辨率工况 · 650×1414 脏污触碰反馈测试')">
              <div class="w-full aspect-phone bg-slate-900/5 rounded-xl overflow-hidden mb-1 flex items-center justify-center">
                <img src="./assets/candidates/home_cat_dirty_tap.png" class="no-crop-img" alt="中模触控">
              </div>
              <div class="text-[9px] font-bold text-slate-700 font-mono truncate">DIRTY_TAP_MID</div>
              <div class="text-[8px] text-slate-400 font-mono">650×1414 (0.460)</div>
            </div>
            <div class="bg-slate-50 p-2 rounded-2xl border border-slate-200 cursor-pointer hover:border-amber-400 transition-all" onclick="inspectImage('./assets/candidates/home_cat_touch_screen.png', '中分辨率工况 · 851×1849 屏幕交互贴合样张')">
              <div class="w-full aspect-phone bg-slate-900/5 rounded-xl overflow-hidden mb-1 flex items-center justify-center">
                <img src="./assets/candidates/home_cat_touch_screen.png" class="no-crop-img" alt="中模贴合">
              </div>
              <div class="text-[9px] font-bold text-slate-700 font-mono truncate">TOUCH_SCR_MID</div>
              <div class="text-[8px] text-slate-400 font-mono">851×1849 (0.460)</div>
            </div>
          </div>
        </div>

""" + candidates_insert_anchor
code = code.replace(candidates_insert_anchor, candidates_new_section)

# 4. In zone-bom: Add 4 Vital Status Badges and Hero Cat Cutouts & App Icons & Feishu Badge
bom_insert_anchor = """        <!-- Sub-cluster 3: Quick Launch System Tiles -->"""
bom_new_section = """        <!-- Sub-cluster 2.5: 4 Vital Health Status Badges & Hero Cat Character Cutouts -->
        <div class="mb-6">
          <div class="flex items-center justify-between mb-3">
            <span class="text-xs font-black text-slate-700 font-mono flex items-center gap-1.5 uppercase">
              <span class="w-2 h-2 rounded-full bg-emerald-500"></span>
              <span>SUB-CLUSTER 2.5 · 四大生命体征状态微章与老马高精度立绘无损切图 (1:1 正方体征 & 自然立绘透视 · 零剪裁)</span>
            </span>
            <span class="text-[10px] font-mono text-slate-400">8 ASSETS · 100% UNPROCESSED</span>
          </div>
          <div class="grid grid-cols-8 gap-3">
            <!-- 4 Vital Status Badges (1254x1254, 1:1 Square) -->
            <div class="bg-slate-50 p-2 rounded-2xl border border-slate-200 cursor-pointer hover:border-emerald-400 transition-all text-center" onclick="inspectImage('./assets/app_assets/generated/status_food.png', '体征微章 · 饱食度正常指数 (1254×1254 · 1:1)')">
              <div class="w-12 h-12 cleanroom-pad rounded-xl mx-auto mb-1 flex items-center justify-center p-1 border border-slate-200">
                <img src="./assets/app_assets/generated/status_food.png" class="no-crop-img" alt="饱食度">
              </div>
              <div class="text-[9px] font-black text-slate-800 font-mono truncate">STATUS_FOOD</div>
              <div class="text-[8px] text-slate-400 font-mono">1:1 正方体征</div>
            </div>
            <div class="bg-slate-50 p-2 rounded-2xl border border-slate-200 cursor-pointer hover:border-emerald-400 transition-all text-center" onclick="inspectImage('./assets/app_assets/generated/status_water.png', '体征微章 · 饮水含水量达标 (1254×1254 · 1:1)')">
              <div class="w-12 h-12 cleanroom-pad rounded-xl mx-auto mb-1 flex items-center justify-center p-1 border border-slate-200">
                <img src="./assets/app_assets/generated/status_water.png" class="no-crop-img" alt="饮水">
              </div>
              <div class="text-[9px] font-black text-slate-800 font-mono truncate">STATUS_WATER</div>
              <div class="text-[8px] text-slate-400 font-mono">1:1 正方体征</div>
            </div>
            <div class="bg-slate-50 p-2 rounded-2xl border border-slate-200 cursor-pointer hover:border-emerald-400 transition-all text-center" onclick="inspectImage('./assets/app_assets/generated/status_litter.png', '体征微章 · 猫砂洁净排泄指标 (1254×1254 · 1:1)')">
              <div class="w-12 h-12 cleanroom-pad rounded-xl mx-auto mb-1 flex items-center justify-center p-1 border border-slate-200">
                <img src="./assets/app_assets/generated/status_litter.png" class="no-crop-img" alt="猫砂">
              </div>
              <div class="text-[9px] font-black text-slate-800 font-mono truncate">STATUS_LITTER</div>
              <div class="text-[8px] text-slate-400 font-mono">1:1 正方体征</div>
            </div>
            <div class="bg-slate-50 p-2 rounded-2xl border border-slate-200 cursor-pointer hover:border-emerald-400 transition-all text-center" onclick="inspectImage('./assets/app_assets/generated/status_bath.png', '体征微章 · 毛发清洁洗护指数 (1254×1254 · 1:1)')">
              <div class="w-12 h-12 cleanroom-pad rounded-xl mx-auto mb-1 flex items-center justify-center p-1 border border-slate-200">
                <img src="./assets/app_assets/generated/status_bath.png" class="no-crop-img" alt="洗护">
              </div>
              <div class="text-[9px] font-black text-slate-800 font-mono truncate">STATUS_BATH</div>
              <div class="text-[8px] text-slate-400 font-mono">1:1 正方体征</div>
            </div>

            <!-- Hero Cat Cutouts (Natural Alpha Ratio) -->
            <div class="bg-slate-50 p-2 rounded-2xl border border-slate-200 cursor-pointer hover:border-indigo-400 transition-all text-center" onclick="inspectImage('./assets/app_assets/hero_cat_sitting_tight.png', '立绘切图 · 老马紧凑正坐形态 (841×1112 · 0.756)')">
              <div class="w-12 h-12 cleanroom-pad rounded-xl mx-auto mb-1 flex items-center justify-center p-1 border border-slate-200">
                <img src="./assets/app_assets/hero_cat_sitting_tight.png" class="no-crop-img" alt="正坐立绘">
              </div>
              <div class="text-[9px] font-black text-slate-800 font-mono truncate">HERO_SITTING</div>
              <div class="text-[8px] text-slate-400 font-mono">841×1112 原型</div>
            </div>
            <div class="bg-slate-50 p-2 rounded-2xl border border-slate-200 cursor-pointer hover:border-indigo-400 transition-all text-center" onclick="inspectImage('./assets/app_assets/hero_cat_carrier_tight.png', '立绘切图 · 老马外出猫包形态 (1018×1112 · 0.916)')">
              <div class="w-12 h-12 cleanroom-pad rounded-xl mx-auto mb-1 flex items-center justify-center p-1 border border-slate-200">
                <img src="./assets/app_assets/hero_cat_carrier_tight.png" class="no-crop-img" alt="猫包立绘">
              </div>
              <div class="text-[9px] font-black text-slate-800 font-mono truncate">HERO_CARRIER</div>
              <div class="text-[8px] text-slate-400 font-mono">1018×1112 原型</div>
            </div>

            <!-- App Icon & Feishu Badge -->
            <div class="bg-slate-50 p-2 rounded-2xl border border-slate-200 cursor-pointer hover:border-blue-400 transition-all text-center" onclick="inspectImage('./assets/candidates/app_icon_preview.png', '品牌应用图标 · 660×660 原生矢量渲染 (1:1)')">
              <div class="w-12 h-12 cleanroom-pad rounded-xl mx-auto mb-1 flex items-center justify-center p-1 border border-slate-200">
                <img src="./assets/candidates/app_icon_preview.png" class="no-crop-img" alt="应用图标">
              </div>
              <div class="text-[9px] font-black text-slate-800 font-mono truncate">APP_ICON</div>
              <div class="text-[8px] text-slate-400 font-mono">660×660 · 1:1</div>
            </div>
            <div class="bg-slate-50 p-2 rounded-2xl border border-slate-200 cursor-pointer hover:border-cyan-400 transition-all text-center" onclick="inspectImage('./assets/app_assets/ic_board_feishu_badge.png', '系统配件 · 飞书多维协作角标道具 (224×212)')">
              <div class="w-12 h-12 cleanroom-pad rounded-xl mx-auto mb-1 flex items-center justify-center p-1 border border-slate-200">
                <img src="./assets/app_assets/ic_board_feishu_badge.png" class="no-crop-img" alt="飞书角标">
              </div>
              <div class="text-[9px] font-black text-slate-800 font-mono truncate">FEISHU_BADGE</div>
              <div class="text-[8px] text-slate-400 font-mono">224×212 配件</div>
            </div>
          </div>
        </div>

""" + bom_insert_anchor
code = code.replace(bom_insert_anchor, bom_new_section)

# 5. In zone-shaders: Add btn_archive_art.png and btn_rank_art.png
shader_insert_anchor = """        </div>
      </div>

      <!-- ===================================================================== -->
      <!-- ZONE SOUTH (南部总成"""

shader_new_items = """          <!-- Texture 07: Archive Art Shader Texture (1.5:1) -->
          <div class="bg-slate-50 p-3 rounded-2xl border border-slate-200 cursor-pointer hover:border-rose-400 transition-all" onclick="inspectImage('./assets/app_assets/generated/btn_archive_art.png', 'Shader 贴图 07 · 手账艺术光影着色图 (1536×1024 · 1.5:1)')">
            <div class="w-full aspect-wide-1-5 bg-slate-900/5 rounded-xl overflow-hidden mb-2 flex items-center justify-center">
              <img src="./assets/app_assets/generated/btn_archive_art.png" class="no-crop-img" alt="btn_archive_art">
            </div>
            <div class="text-xs font-bold text-slate-800 font-mono">BTN_ARCHIVE_ART (1.5:1)</div>
            <div class="text-[10px] text-slate-400 font-mono mt-0.5">1536×1024 渐变漫反射艺术贴图</div>
          </div>

          <!-- Texture 08: Rank Art Shader Texture (1.5:1) -->
          <div class="bg-slate-50 p-3 rounded-2xl border border-slate-200 cursor-pointer hover:border-rose-400 transition-all" onclick="inspectImage('./assets/app_assets/generated/btn_rank_art.png', 'Shader 贴图 08 · 排行榜艺术高光着色图 (1536×1024 · 1.5:1)')">
            <div class="w-full aspect-wide-1-5 bg-slate-900/5 rounded-xl overflow-hidden mb-2 flex items-center justify-center">
              <img src="./assets/app_assets/generated/btn_rank_art.png" class="no-crop-img" alt="btn_rank_art">
            </div>
            <div class="text-xs font-bold text-slate-800 font-mono">BTN_RANK_ART (1.5:1)</div>
            <div class="text-[10px] text-slate-400 font-mono mt-0.5">1536×1024 金属拉丝高光艺术贴图</div>
          </div>
""" + shader_insert_anchor
code = code.replace(shader_insert_anchor, shader_new_items)

# Write updated code to index.html and generate_ultimate_canvas.py
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(code)

with open("/Users/bingo/Code/LYi/projects/laoma-engine-showcase/generate_ultimate_canvas.py", "w", encoding="utf-8") as f:
    f.write(code)

print("Full showcase updated and generated successfully!")
