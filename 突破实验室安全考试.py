from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time
import re
answer_source = '''
				
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      1、<span style="color:#990000">[判断题]</span> <strong>发生化学事故后，对有毒的衣物应及时进行无毒化处理。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      2、<span style="color:#990000">[判断题]</span> <strong>乙醚的爆炸极限是：1.9％～48％。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      3、<span style="color:#990000">[判断题]</span> <strong>氢气的爆炸极限是：4％～75％。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      4、<span style="color:#990000">[判断题]</span> <strong>CO经呼吸道进入血液后，立即与血红蛋白结合形成碳氧血红蛋白，CO与血红蛋白的亲和力比氧大，致使血携氧能力下降，同时碳氧血红蛋白的解离速度却比氧合血红蛋白的解离慢3600倍，且碳氧血红蛋白的存在影响氧合血红蛋白的解离，阻碍了氧的释放，导致低氧血症，引起组织缺氧。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      5、<span style="color:#990000">[判断题]</span> <strong>从消防观点来说,液体闪点就是可能引起火灾的最低温度。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      6、<span style="color:#990000">[判断题]</span> <strong>燃点越低的物品越安全。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  错误              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      7、<span style="color:#990000">[判断题]</span> <strong>铅被加热到400℃以上就有大量铅蒸汽逸出，在空气中迅速氧化为氧化铅，形成烟尘，易被人体吸入，造成铅中毒。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      8、<span style="color:#990000">[判断题]</span> <strong>毒物在科研生产中以气体、蒸气、烟、尘、雾等形态存在，其中气体、蒸气为分子状态，可直接进入人体肺泡。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      9、<span style="color:#990000">[判断题]</span> <strong>皮肤接触活泼金属(如钾、钠)，可用大量水冲洗。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  错误              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      10、<span style="color:#990000">[判断题]</span> <strong>实验室的药品和设备一定要标明其名称，以免误用。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      11、<span style="color:#990000">[判断题]</span> <strong>发生化学事故后，应向上风或侧上风方向迅速撤离现场。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      12、<span style="color:#990000">[判断题]</span> <strong>使用剧毒药品时应该配备个人防护用具，做好应急援救预案。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      13、<span style="color:#990000">[判断题]</span> <strong>砷的解毒剂是二巯基丙醇，由肌肉注射即可解毒。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      14、<span style="color:#990000">[判断题]</span> <strong>有毒化学药品溅在皮肤上时，可用乙醇等有机溶剂擦洗。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  错误              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      15、<span style="color:#990000">[判断题]</span> <strong>身上着火被熄灭后,应马上把粘在皮肤上的衣物脱下来。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  错误              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      16、<span style="color:#990000">[判断题]</span> <strong>当被烧伤时,正确的急救方法应该是以最快的速度用冷水冲洗烧伤部位。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      17、<span style="color:#990000">[判断题]</span> <strong>含碱性洗涤剂的水可以清洗掉水果蔬菜表面的农药。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      18、<span style="color:#990000">[判断题]</span> <strong>在实验室允许口尝鉴定试剂和未知物。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  错误              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      19、<span style="color:#990000">[判断题]</span> <strong>可以在敞口容器中存放易爆物质。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  错误              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      20、<span style="color:#990000">[判断题]</span> <strong>金属钠、钾可以存放在水中，以避免与空气接触。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  错误              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      21、<span style="color:#990000">[判断题]</span> <strong>SnCl2、FeSO4、Na2SO3与空气接触易逐渐被氧化，须密封保存。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      22、<span style="color:#990000">[判断题]</span> <strong>NH4NO3受热后易分解，但放出的气体无害。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  错误              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      23、<span style="color:#990000">[判断题]</span> <strong>SO2易溶于水，大量吸入会引起喉水肿，肺水肿、窒息。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      24、<span style="color:#990000">[判断题]</span> <strong>将醇液直接加入到室温以下的硫酸-硝酸的混酸中不会引起爆炸，而加入到未冷却的硫酸-硝酸的混酸中会引起爆炸。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  错误              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      25、<span style="color:#990000">[判断题]</span> <strong>过氧化物、高氯酸盐、叠氮铅、乙炔铜、三硝基甲苯等属于易爆物质，受震或受热可发生热爆炸。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      26、<span style="color:#990000">[判断题]</span> <strong>有毒化学品在水中的溶解度越大，其危险性越大。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      27、<span style="color:#990000">[判断题]</span> <strong>液氯钢瓶与液氨钢瓶可以在同库存放。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  错误              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      28、<span style="color:#990000">[判断题]</span> <strong><p>氰化钾、氰化钠、丙烯腈等是剧毒品，进入人体50毫克即可致死，与皮肤接触经伤口进入人体，即可引起严重中毒。</p></strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      29、<span style="color:#990000">[判断题]</span> <strong>Cl2和CO作用生成的光气毒性比Cl2大。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      30、<span style="color:#990000">[判断题]</span> <strong>乙醚、氯仿、笑气（N2O）具有麻醉作用。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      31、<span style="color:#990000">[判断题]</span> <strong>汞及其化合物、砷及其无机化合物、黄磷、碘甲烷、甲基丙烯酸甲酯、氰化物等具有剧毒性。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      32、<span style="color:#990000">[判断题]</span> <strong>苯、三硝基甲苯、二硫化碳、丙烯腈、四氯化碳、甲醛、苯胺、氯丙烯、溴甲烷、环氧氯丙烷、光气、一氧化碳等具有高毒性。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      33、<span style="color:#990000">[判断题]</span> <strong>丙酮、氢氧化钠、氨等具有低毒性。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      34、<span style="color:#990000">[判断题]</span> <strong>打开易挥发或浓酸、浓碱试剂的瓶塞时，瓶口不要对着脸部或其他人，宜在通风橱中进行。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      35、<span style="color:#990000">[判断题]</span> <strong>溴（水）是腐蚀性极强的物质，必须在通风柜中操作，并注意安全。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      36、<span style="color:#990000">[判断题]</span> <strong>做减压蒸馏时，如果没有梨形接收瓶，可用锥形瓶代替。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  错误              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      37、<span style="color:#990000">[判断题]</span> <strong>开启氨水、浓盐酸瓶应该在通风櫉中进行。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      38、<span style="color:#990000">[判断题]</span> <strong>水银温度计破了以后正确的处理是：洒落出来的汞必须立即用滴管、毛刷收集起来，并用水覆盖（最好用甘油），然后在污染处撒上硫磺粉，无液体后（一般约一周时间）方可清扫。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      39、<span style="color:#990000">[判断题]</span> <strong>烧杯、烧瓶及试管等加热时比较安全。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  错误              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      40、<span style="color:#990000">[判断题]</span> <strong>如发现水泵漏水，可以不用切断电源，待实验完毕后再报修。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  错误              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      41、<span style="color:#990000">[判断题]</span> <strong>当发生强碱溅洒事故时，应用固体硼酸粉撒盖溅洒区，扫净并报告有关工作人员。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      42、<span style="color:#990000">[判断题]</span> <strong>装有易燃液体的器皿可置于日光下。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  错误              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      43、<span style="color:#990000">[判断题]</span> <strong>急性中毒发生时，救护人员在抢救前要做好自身呼吸系统和皮肤的防护，以免自身中毒、使事故扩大。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      44、<span style="color:#990000">[判断题]</span> <strong>给液体加热时，可以先开始加热，等接近沸腾时再加入沸石。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  错误              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      45、<span style="color:#990000">[判断题]</span> <strong>酒精灯内的酒精量最多可加九分满。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  错误              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      46、<span style="color:#990000">[判断题]</span> <strong>可以将乙炔与氧气混放在一个房间。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  错误              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      47、<span style="color:#990000">[判断题]</span> <strong>对于含氟废液可以进行如下处理：加入石灰使生成氟化钙沉淀。 </strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      48、<span style="color:#990000">[判断题]</span> <strong>在实验室内一切有可能产生毒性蒸气的工作必须在通风橱中进行，并有良好的排风设备。  </strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      49、<span style="color:#990000">[判断题]</span> <strong>能相互反应产生有毒气体的废液，不得倒入同一收集桶中。若某种废液倒入收集桶会发生危险，则应单独暂存于一容器中，并贴上标签。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      50、<span style="color:#990000">[判断题]</span> <strong>发生危险化学品事故后,应该向上风方向疏散。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      51、<span style="color:#990000">[判断题]</span> <strong>使用危险化学品单位应当制定本单位事故应急救援预案，配备应急救援人员和必要的应急救援器材、设备，并定期组织演练。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      52、<span style="color:#990000">[判断题]</span> <strong>收集、贮存危险废物，必须按照危险废物特性分类进行。禁止混合收集、贮存、运输、处置性质不相容而未经安全性处置的危险废物。 </strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      53、<span style="color:#990000">[判断题]</span> <strong>一氧化碳泄漏，应先施行通风，以驱散一氧化碳气体，并切断一氧化碳泄漏源。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      54、<span style="color:#990000">[判断题]</span> <strong>酚灼伤皮肤时，应立即脱掉被污染衣物，用10%酒精反复擦拭，再用大量清水冲洗，直至无酚味为止，然后用饱和硫酸钠湿敷。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      55、<span style="color:#990000">[判断题]</span> <strong>眼部碱灼伤时，应立即用大量清水或生理盐水进行彻底冲洗，冲洗时必须将上下眼睑拉开，水不要流经未伤的眼睛，不可直接冲击眼球，然后可用2%～3%硼酸溶液进一步冲洗。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      56、<span style="color:#990000">[判断题]</span> <strong>生产、储存和使用危险化学品的单位，应当在生产、储存和使用场所设置报警装置。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      57、<span style="color:#990000">[判断题]</span> <strong>可以使用明火（如：电炉、煤气）或没有控温装置的加热设备直接加热有机溶剂，进行重结晶或溶液浓缩操作。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  错误              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      58、<span style="color:#990000">[判断题]</span> <strong>冰箱内禁止存放危险化学物品，如果确需存放，则必须注意容器绝对密封，严防泄漏。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      59、<span style="color:#990000">[判断题]</span> <strong>存有易燃易爆物品的实验室禁止使用明火，如需加热可使用封闭式电炉、加热套或可加热磁力搅拌器。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      60、<span style="color:#990000">[判断题]</span> <strong>实验产生的废液（废酸、废碱等）和废弃固体物质可直接倒入下水道或普通垃圾桶。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  错误              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      61、<span style="color:#990000">[判断题]</span> <strong>凡涉及有害或有刺激性气体的实验应在通风柜内进行。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      62、<span style="color:#990000">[判断题]</span> <strong>受阳光照射易燃烧、易爆炸或产生有毒气体的化学危险品和桶装、罐装等易燃液体、气体应当在阴凉通风的地点存放。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      63、<span style="color:#990000">[判断题]</span> <strong>化学危险物品应当分类、分项存放，还原性试剂与氧化剂、酸与碱类腐蚀剂等不得混放，相互之间保持安全距离。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      64、<span style="color:#990000">[判断题]</span> <strong>有机废物、浓酸或浓碱废液等倒入水槽，只要加大量的自来水将之冲稀即可。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  错误              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      65、<span style="color:#990000">[判断题]</span> <strong>酸、碱、盐水溶液使用后，经自来水稀释后可直接排入下水道。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  错误              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      66、<span style="color:#990000">[判断题]</span> <strong>各实验室对所产生的化学废弃物必须要实行集中分类存放，贴好标签，然后送学校中转站，统一处置。 </strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      67、<span style="color:#990000">[单选题]</span> <strong>以下什么物质引起的皮肤灼伤禁用水洗?</strong> （分值1.0）<br/>
      <ul><li>A. 五氧化二磷<br />
B. 五硫化磷<br />
C. 五氯化磷<br />
D. 以上都是</li></ul>              你未作答
            标准答案：
                  D
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      68、<span style="color:#990000">[单选题]</span> <strong>铝粉、保险粉自燃时如何扑救？</strong> （分值1.0）<br/>
      <ul><li>A. 用水灭火  <br />
B. 用泡沫灭火器  <br />
C. 用干粉灭火器  <br />
D. 用干砂子灭火</li></ul>              你未作答
            标准答案：
                  D
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      69、<span style="color:#990000">[单选题]</span> <strong>容器中的溶剂或易燃化学品发生燃烧应如何处理？</strong> （分值1.0）<br/>
      <ul><li>A. 用灭火器灭火或加砂子灭火  <br />
B. 加水灭火  <br />
C. 用不易燃的瓷砖、玻璃片盖住瓶口  <br />
D. 用湿抹布盖住瓶口</li></ul>              你未作答
            标准答案：
                  A
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      70、<span style="color:#990000">[单选题]</span> <strong>使用碱金属引起燃烧应如何处理？</strong> （分值1.0）<br/>
      <ul><li>A. 马上使用灭火器灭火  <br />
B. 马上向燃烧处浇水灭火<br />
C. 马上用石棉布盖砂子盖住燃烧处，尽快移去临近其它溶剂，关闭热源和电源，再用灭火器灭火<br />
D. 以上都对</li></ul>              你未作答
            标准答案：
                  C
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      71、<span style="color:#990000">[单选题]</span> <strong>当不慎把少量浓硫酸滴在皮肤上(在皮肤上没形成挂液)时，正确的处理方法是：</strong> （分值1.0）<br/>
      <ul><li>A. 用酒精棉球擦 <br />
B. 不作处理，马上去医院<br />
C. 用碱液中和后，用水冲洗 <br />
D. 用水直接冲洗</li></ul>              你未作答
            标准答案：
                  D
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      72、<span style="color:#990000">[单选题]</span> <strong>皮肤若被低温（如固体二氧化碳、液氮）冻伤，应：</strong> （分值1.0）<br/>
      <ul><li>A. 马上送医院<br />
B. 用温水慢慢恢复体温<br />
C. 用火烘烤<br />
D. 应尽快浸入热水</li></ul>              你未作答
            标准答案：
                  B
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      73、<span style="color:#990000">[单选题]</span> <strong>不具有强酸性和强腐蚀性的物质是：</strong> （分值1.0）<br/>
      <ul><li>A. 氢氟酸    <br />
B. 碳酸   <br />
C. 稀硫酸    <br />
D. 稀硝酸</li></ul>              你未作答
            标准答案：
                  B
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      74、<span style="color:#990000">[单选题]</span> <strong>危险化学品的毒害包括：</strong> （分值1.0）<br/>
      <ul><li>A.皮肤腐蚀性/刺激性，眼损伤/眼刺激<br />
B.急性中毒致死，器官或呼吸系统损伤，生殖细胞突变性，致癌性<br />
C.水环境危害性, 放射性危害<br />
D.以上都是</li></ul>              你未作答
            标准答案：
                  D
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      75、<span style="color:#990000">[单选题]</span> <strong>下面哪些物质彼此混合时，不容易引起火灾？</strong> （分值1.0）<br/>
      <ul><li>A. 活性炭与硝酸铵<br />
B. 金属钾、钠和煤油<br />
C. 磷化氢、硅化氢、烷基金属、白磷等物质与空气接触<br />
D. 可燃性物质（木材、织物等）与浓硫酸</li></ul>              你未作答
            标准答案：
                  B
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      76、<span style="color:#990000">[单选题]</span> <strong>苯乙烯、乙酸乙烯酯应如何存放？</strong> （分值1.0）<br/>
      <ul><li>A. 放在防爆冰箱里 <br />
B. 和其它试剂混放  <br />
C. 放在通风橱内<br />
D. 放在密闭的柜子中</li></ul>              你未作答
            标准答案：
                  A
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      77、<span style="color:#990000">[单选题]</span> <strong>氮氧化物主要伤害人体的：</strong> （分值1.0）<br/>
      <ul><li>A. 眼、上呼吸道     <br />
B. 呼吸道深部的细支气管、肺泡<br />
C. 皮肤<br />
D. 消化道</li></ul>              你未作答
            标准答案：
                  B
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      78、<span style="color:#990000">[单选题]</span> <strong>关于存储化学品说法错误的是：</strong> （分值1.0）<br/>
      <ul><li>A. 化学危险物品应当分类、分项存放，相互之间保持安全距离<br />
B. 遇火、遇潮容易燃烧、爆炸或产生有毒气体的化学危险品，不得在露天、潮湿、漏雨或低洼容易积水的地点存放<br />
C. 受阳光照射易燃烧、易爆炸或产生有毒气体的化学危险品和桶装、罐装等易燃液体、气体应当在密闭地点存放<br />
D. 防护和灭火方法相互抵触的化学危险品，不得在同一仓库或同一储存室存放</li></ul>              你未作答
            标准答案：
                  C
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      79、<span style="color:#990000">[单选题]</span> <strong>关于存放自燃性试剂说法错误的是：</strong> （分值1.0）<br/>
      <ul><li>A. 单独储存    <br />
B. 储存于通风、阴凉、干燥处    <br />
C. 存放于试剂架上<br />
D. 远离明火及热源，防止太阳直射</li></ul>              你未作答
            标准答案：
                  C
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      80、<span style="color:#990000">[单选题]</span> <strong>活泼金属应存放在何处？</strong> （分值1.0）<br/>
      <ul><li>A. 密封容器中并放入冰箱 <br />
B. 密封容器中并放入干燥器   <br />
C. 泡在煤油里密封避光保存<br />
D. 密封容器中并放入密闭柜子内</li></ul>              你未作答
            标准答案：
                  C
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      81、<span style="color:#990000">[单选题]</span> <strong>金属Hg具有高毒性，常温下挥发情况如何？</strong> （分值1.0）<br/>
      <ul><li>A. 不挥发  <br />
B. 慢慢挥发  <br />
C. 很快挥发<br />
D. 需要在一定条件下才会挥发</li></ul>              你未作答
            标准答案：
                  B
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      82、<span style="color:#990000">[单选题]</span> <strong>为了安全，须贮存于煤油中的金属是：</strong> （分值1.0）<br/>
      <ul><li>A. 钠 <br />
B. 铝<br />
C. 铁 <br />
D. 钙</li></ul>              你未作答
            标准答案：
                  A
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      83、<span style="color:#990000">[单选题]</span> <strong>下列哪种物质与乙醇混溶时易发生爆炸？</strong> （分值1.0）<br/>
      <ul><li>A. 盐酸 <br />
B. 乙醚      <br />
C. 高氯酸 <br />
D. 丙酮</li></ul>              你未作答
            标准答案：
                  C
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      84、<span style="color:#990000">[单选题]</span> <strong>下列实验室操作及安全的叙述，正确的是？</strong> （分值1.0）<br/>
      <ul><li>A. 实验后所取用剩余的药品应小心倒回原容器，以免浪费。<br />
B. 当强碱溶液溅出时，可先用大量的水稀释后再处理。<br />
C. 温度计破碎流出的汞，宜洒上盐酸使反应为氯化汞后再弃之。</li></ul>              你未作答
            标准答案：
                  B
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      85、<span style="color:#990000">[单选题]</span> <strong>不慎发生意外，下列哪个操作是正确的？</strong> （分值1.0）<br/>
      <ul><li>A. 如果不慎将化学品弄洒或污染，立即自行回收或者清理现场，以免对他人产生危险<br />
B. 任何时候见到他人洒落的液体应及时用抹布抹去，以免发生危险<br />
C. pH值中性即意味着液体是水，自行清理即可 <br />
D. 不慎将化学试剂弄到衣物和身体上，立即用大量清水冲洗10－15分钟</li></ul>              你未作答
            标准答案：
                  D
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      86、<span style="color:#990000">[单选题]</span> <strong>离心操作时，为防液体溢出，离心管中样品装量不能超过离心管体积的多少？</strong> （分值1.0）<br/>
      <ul><li>A．2/3<br />
B. 1/3<br />
C. 1/2<br />
D. 3/4</li></ul>              你未作答
            标准答案：
                  A
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      87、<span style="color:#990000">[单选题]</span> <strong>普通塑料、有机玻璃制品的加热温度不能超过：</strong> （分值1.0）<br/>
      <ul><li>A．40℃<br />
B. 60℃<br />
C. 80℃<br />
D. 100℃</li></ul>              你未作答
            标准答案：
                  B
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      88、<span style="color:#990000">[单选题]</span> <strong>取用试剂时，错误的说法是：</strong> （分值1.0）<br/>
      <ul><li>A. 不能用手接触试剂，以免危害健康和沾污试剂<br />
B. 瓶塞应倒置桌面上，以免弄脏，取用试剂后，立即盖严，将试剂瓶放回原处，标签朝外<br />
C. 要用干净的药匙取固体试剂，用过的药匙要洗净擦干才能再用<br />
D. 多取的试剂可倒回原瓶，避免浪费</li></ul>              你未作答
            标准答案：
                  D
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      89、<span style="color:#990000">[单选题]</span> <strong>实验室内使用乙炔气时，说法正确的是：</strong> （分值1.0）<br/>
      <ul><li>A. 室内不可有明火，不可有产生电火花的电器   <br />
B. 房间应密闭  <br />
C. 室内应有高湿度 <br />
D. 乙炔气可用铜管道输送</li></ul>              你未作答
            标准答案：
                  A
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      90、<span style="color:#990000">[单选题]</span> <strong>室温较高时，有些试剂如氨水等，打开瓶塞的瞬间很易冲出气液流，应先如何处理，再打开瓶塞？</strong> （分值1.0）<br/>
      <ul><li>A. 先将试剂瓶在热水中浸泡一段时间      <br />
B. 振荡一段时间<br />
C. 先将试剂瓶在冷水中浸泡一段时间<br />
D. 先将试剂瓶颠倒一下</li></ul>              你未作答
            标准答案：
                  C
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      91、<span style="color:#990000">[单选题]</span> <strong>往玻璃管上套橡皮管（塞）时，不正确的做法是：</strong> （分值1.0）<br/>
      <ul><li>A. 管端应烧圆滑 <br />
B. 用布裹手或带厚手套，以防割伤手 <br />
C. 可以使用薄壁玻管 <br />
D. 加点水或润滑剂</li></ul>              你未作答
            标准答案：
                  D
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      92、<span style="color:#990000">[单选题]</span> <strong>稀硫酸溶液的正确制备方法是：</strong> （分值1.0）<br/>
      <ul><li>A. 在搅拌下，加水于浓硫酸中 <br />
B. 在搅拌下，加浓硫酸于水中<br />
C. 水加于浓硫酸，或浓硫酸加于水都无所谓 <br />
D. 水与浓硫酸两者一起倒入容器混合</li></ul>              你未作答
            标准答案：
                  B
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      93、<span style="color:#990000">[单选题]</span> <strong>领取剧毒物品时，必须：）</strong> （分值1.0）<br/>
      <ul><li>A．双人领用(其中一人必须是实验室的教师)<br />
B．单人领用<br />
C．双人领用(两人都是实验室的学生)</li></ul>              你未作答
            标准答案：
                  A
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      94、<span style="color:#990000">[单选题]</span> <strong>有些固体化学试剂（如硫化磷、赤磷、镁粉等）与氧化剂接触或在空气中受热、受冲击或磨擦能引起急剧燃烧，甚至爆炸。使用这些化学试剂时，要注意什么：</strong> （分值1.0）<br/>
      <ul><li>A. 要注意周围环境湿度不要太高  <br />
B. 周围温度一般不要超过30℃，最好在20℃以下    <br />
C. 不要与强氧化剂接触<br />
D. 以上都是</li></ul>              你未作答
            标准答案：
                  D
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      95、<span style="color:#990000">[单选题]</span> <strong>处理使用后的废液时，下列哪个说法是错误的？</strong> （分值1.0）<br/>
      <ul><li>A. 不明的废液不可混合收集存放<br />
B. 废液不可任意处理<br />
C. 禁止将水以外的任何物质倒入下水道，以免造成环境污染和处理人员危险<br />
D. 少量废液用水稀释后，可直接倒入下水道</li></ul>              你未作答
            标准答案：
                  D
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      96、<span style="color:#990000">[单选题]</span> <strong>处置实验过程产生的剧毒药品废液，说法错误的是：</strong> （分值1.0）<br/>
      <ul><li>A. 妥善保管  <br />
B. 不得随意丢弃、掩埋  <br />
C. 集中保存，统一处理<br />
D. 稀释后用大量水冲净</li></ul>              你未作答
            标准答案：
                  D
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      97、<span style="color:#990000">[单选题]</span> <strong>实验室冰箱和超低温冰箱使用注意事项错误的是：</strong> （分值1.0）<br/>
      <ul><li>A. 定期除霜、清理，清理后要对内表面进行消毒<br />
B. 储存的所有容器，应当标明物品名称、储存日期和储存者姓名<br />
C. 除非有防爆措施，否则冰箱内不能放置易燃易爆化学品溶液，冰箱门上应注明这一点<br />
D. 可以在冰箱内冷冻食品和水</li></ul>              你未作答
            标准答案：
                  D
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      98、<span style="color:#990000">[单选题]</span> <strong>下列加热热源，化学实验室原则不得使用的是：</strong> （分值1.0）<br/>
      <ul><li>A. 明火电炉<br />
B. 水浴、蒸汽浴   <br />
C. 油浴、沙浴、盐浴   <br />
D. 电热板、电热套</li></ul>              你未作答
            标准答案：
                  A
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      99、<span style="color:#990000">[单选题]</span> <strong>易燃化学试剂存放和使用的注意事项正确是：</strong> （分值1.0）<br/>
      <ul><li>A. 要求单独存放于阴凉通风处       <br />
B. 放在冰箱中时，要使用防爆冰箱<br />
C. 远离火源，绝对不能使用明火加热<br />
D. 以上都是</li></ul>              你未作答
            标准答案：
                  D
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      100、<span style="color:#990000">[单选题]</span> <strong>用过的废洗液应如何处理？</strong> （分值1.0）<br/>
      <ul><li>A. 可直接倒入下水道 <br />
B. 作为废液交相关部门统一处理 <br />
C. 可以用来洗厕所<br />
D. 随意处置</li></ul>              你未作答
            标准答案：
                  B
              
              </div>
                      
              <div class="nav">
                   <ul>
                	<li><img src="/template/images/arrow1_085.gif" /> <a href="/">返回考试首页</a></li>
                   </ul>
                </div>   
              
          </div>

<div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      1、<span style="color:#990000">[判断题]</span> <strong>实验时,禁止用口吸方式移液。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      2、<span style="color:#990000">[判断题]</span> <strong>生物废弃物应置于专用的、有标记的容器内。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      3、<span style="color:#990000">[判断题]</span> <strong>为了确保动物实验的正常开展,应严格控制无关人员、昆虫及野生动物、病原微生物进入实验室。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      4、<span style="color:#990000">[判断题]</span> <strong>生物实验中的一次性手套及沾染EB致癌物质的物品，可以丢弃在普通垃圾箱内。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  错误              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      5、<span style="color:#990000">[判断题]</span> <strong>使用U盘拷贝资料，应先对U盘杀毒，防止病毒感染 。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      6、<span style="color:#990000">[判断题]</span> <strong>测试数据应进行异地备份。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      7、<span style="color:#990000">[判断题]</span> <strong>有“严禁烟火”警示牌的大楼和实验室，可不必配置必要的消防、冲淋、洗眼、报警和逃生设施和有明显标志。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  错误              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      8、<span style="color:#990000">[判断题]</span> <strong>及时淘汰老化、性能不稳又具有安全隐患的仪器设备（如冰箱10年以上，烘箱12年以上）。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      9、<span style="color:#990000">[判断题]</span> <strong>针头、玻璃、一次性手术刀等利器应在使用后放在耐扎容器中，尖利物容器应在内容物达到三分之二前进行置换处置。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      10、<span style="color:#990000">[判断题]</span> <strong>自然地形跑步时要注意做好缓冲动作，用全脚掌先着地，后蹬程度和前摆高度要小一些。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  错误              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      11、<span style="color:#990000">[判断题]</span> <strong>发生各类案件时应立即报案，妥善保护案发现场，若有人受伤，在救人时应尽可能记住现场破坏前的情况（如手机拍照等）。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      12、<span style="color:#990000">[判断题]</span> <strong>因实验室特殊要求，细胞培养房内用的气体钢瓶可不用固定，只要平时小心就可以。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  错误              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      13、<span style="color:#990000">[判断题]</span> <strong>学生、新员工进实验室之前要参加安全教育和培训，经培训、考核合格后方可进入实验室学习与工作；学生要在老师指导下开展实验研究。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      14、<span style="color:#990000">[判断题]</span> <strong>做实验时要爱护实验设备，同时注意自身的安全，避免发生事故。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      15、<span style="color:#990000">[判断题]</span> <strong>进行需要戴防护眼镜的实验时，戴隐形眼镜的近视者可不戴防护眼镜。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  错误              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      16、<span style="color:#990000">[判断题]</span> <strong>如遇刺激性及神经性中毒，先服牛奶或鸡蛋白使之缓和，再服用硫酸铜溶液（30g溶于一杯水中）催吐。也可以用手指伸入喉部催吐后，立即送往医院。 </strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      17、<span style="color:#990000">[判断题]</span> <strong>实验中溅入口中而尚未下咽的毒物，应立即吐出，并用大量水冲洗口腔。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      18、<span style="color:#990000">[判断题]</span> <strong>如溴滴落到皮肤上，应立即用水冲洗，再用1体积25%的氨水，1体积松节油和10体积（75%）酒精混合液涂敷；也可先用苯甘油除去溴，然后用水冲洗。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      19、<span style="color:#990000">[判断题]</span> <strong>使用手提灭火器时，拨掉保险销，对准着火点根部用力压下压把，灭火剂喷出，就可灭火。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      20、<span style="color:#990000">[判断题]</span> <strong>电气线路着火，要先切断电源，再用干粉灭火器或二氧化碳灭火器灭火，不可直接泼水灭火，以防触电或电气爆炸伤人。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      21、<span style="color:#990000">[判断题]</span> <strong>实验室常用的灭火方法：用水灭火、砂土灭火、灭火器。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      22、<span style="color:#990000">[判断题]</span> <strong>仪器设备用电或线路发生故障着火时，应立即切断现场电源，将人员疏散，并组织人员用灭火器进行灭火。 </strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      23、<span style="color:#990000">[判断题]</span> <strong>隔离灭火法是将可燃物与引火源或氧气隔离开来，可防止火势继续扩大。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      24、<span style="color:#990000">[判断题]</span> <strong>火灾发生后，当所有的逃生线路被大火封锁时，应立即退回室内，用手电筒、挥舞衣物、呼叫等方式向窗外发送求救信号，等待救援。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      25、<span style="color:#990000">[判断题]</span> <strong>火灾发生后，受到火势威胁时，要当机立断披上浸湿的衣物、被褥等向安全出口方向冲去。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      26、<span style="color:#990000">[判断题]</span> <strong>火灾发生后，穿过浓烟逃生时，必须尽量贴近地面，并用湿毛巾捂住口鼻。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      27、<span style="color:#990000">[判断题]</span> <strong>实验室必须配备符合本室要求的消防器材，消防器材要放置在明显或便于拿取的位置。严禁任何人以任何借口把消防器材移作它用。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      28、<span style="color:#990000">[判断题]</span> <strong>可以用潮湿的手碰开关、电线和电器。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  错误              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      29、<span style="color:#990000">[判断题]</span> <strong>消防工作的方针是：“预防为主，防消结合”，实行消防安全责任制。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      30、<span style="color:#990000">[判断题]</span> <strong>建筑物发生火灾时，乘坐电梯疏散即快速又安全省力。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  错误              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      31、<span style="color:#990000">[判断题]</span> <strong>二氧化碳灭火器使用不当，可能会造成冻伤。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      32、<span style="color:#990000">[判断题]</span> <strong>踝关节韧带扭伤以后立即冷敷，加压包扎固定。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      33、<span style="color:#990000">[判断题]</span> <strong>轻微的肌肉拉伤或少量的肌肉纤维的断裂，应立即冷敷，局部加压包扎，抬高肢体。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      34、<span style="color:#990000">[判断题]</span> <strong>出现内伤如挫伤、肌肉拉伤、关节扭伤、滑囊炎、腱鞘炎等24小时内一般用冷敷，加压包扎，抬高受伤的肢体等方法，尽可能减少受伤部位的出血。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      35、<span style="color:#990000">[判断题]</span> <strong>出现肌肉痉挛（抽筋），常见的缓解法是拉长痉挛的肌肉，同时配合局部按摩和点压穴位等方法促进缓解。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      36、<span style="color:#990000">[判断题]</span> <strong>实验室不得乱拉电线，套接接线板。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      37、<span style="color:#990000">[判断题]</span> <strong>实验室安全与卫生检查内容主要包括实验室布置、卫生、水电安全、冰箱与烘箱使用管理、危险品使用与保管、化学与生物废弃物（气、液、固态物）的处置、排污管理、气体钢瓶安全、放射性安全等。 </strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      38、<span style="color:#990000">[判断题]</span> <strong>易燃、易爆气体和助燃气体（氧气等）的钢瓶不得混放在一起，并应远离热源和火源，保持通风。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      39、<span style="color:#990000">[判断题]</span> <strong>实验室冰箱内不得混放容易产生放热反应的化学品。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      40、<span style="color:#990000">[判断题]</span> <strong>实验室内电源根据需要可自行拆装、改线。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  错误              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      41、<span style="color:#990000">[判断题]</span> <strong>不得堵塞实验室逃生通道。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      42、<span style="color:#990000">[判断题]</span> <strong>普通实验室内，不得私自饲养实验动物。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      43、<span style="color:#990000">[判断题]</span> <strong>不得在冰箱、烘箱等加热、产热设备附近放置纸板、化学试剂、气体钢瓶等物品。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      44、<span style="color:#990000">[判断题]</span> <strong>实验室应将相应的规章制度和操作规程挂到墙上或便于取阅的地方。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      45、<span style="color:#990000">[判断题]</span> <strong>实施急救的顺序：若有呼吸心跳停止的，先行复苏，然后是止血、包扎、骨折固定或脱臼复位（固定）、搬运。 </strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      46、<span style="color:#990000">[判断题]</span> <strong>实验室气体钢瓶必须用铁链、钢瓶柜等固定，以防止倾倒引发安全事故。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      47、<span style="color:#990000">[判断题]</span> <strong>在使用高压灭菌锅、烤箱等高压加热设备时，必须有人值守。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      48、<span style="color:#990000">[判断题]</span> <strong>实验进行前要了解实验仪器的使用说明及注意事项，实验过程中要严格按照操作规程进行操作。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      49、<span style="color:#990000">[判断题]</span> <strong>实验室应保持整洁有序，不准喧哗、打闹、抽烟。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      50、<span style="color:#990000">[判断题]</span> <strong>禁止邮寄属于国家秘密的文件、资料和其他物品出境，禁止非法携运属于国家秘密的文件、资料和其他物品出境。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      51、<span style="color:#990000">[判断题]</span> <strong>国家秘密载体是指以文字、数据、符号、图形、图像、声音等方式记载国家秘密信息的纸介质、磁介质、光盘等各类物品。磁介质载体包括计算机硬盘、软盘和录音带、录像带等。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      52、<span style="color:#990000">[判断题]</span> <strong>可以用湿布擦电源开关。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  错误              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      53、<span style="color:#990000">[判断题]</span> <strong>大型仪器使用中，应注意仪器设备的接地、电磁辐射、网络等安全事项，避免事故发生。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      54、<span style="color:#990000">[判断题]</span> <strong>《中华人民共和国传染病防治法》由中华人民共和国第十届全国人民代表大会常务委员会第十一次会议于2004年8月28日修订通过。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      55、<span style="color:#990000">[判断题]</span> <strong>一般的实验室只要干净、卫生情况良好，就可以饲养动物或进行动物实验。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  错误              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      56、<span style="color:#990000">[判断题]</span> <strong>触电时，不可人去拉（可用木棒把伤员挑开），应立即切断电源，然后先做人工呼吸，再做心脏按压，同时报120送医院进行处理。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      57、<span style="color:#990000">[判断题]</span> <strong>急救时伤口包扎越紧越好。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  错误              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      58、<span style="color:#990000">[判断题]</span> <strong>强酸灼伤时，必须先用大量流水彻底冲洗，然后在皮肤上擦拭碱性药物，否则会加重皮肤损伤。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      59、<span style="color:#990000">[判断题]</span> <strong>胸外心脏挤压法：救护者跪在触电者一侧或骑跪在其腰部两侧，两手相迭，手掌根部放在伤者心窝上方、胸骨下，掌根用力垂直向下挤压，压出心脏里面的血液，挤压后迅速松开，胸部自动复原，血液充满心脏，以每分钟60次速度进行。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      60、<span style="color:#990000">[判断题]</span> <strong>用手搬运重物时，应先以半蹲姿势，抓牢重物，然后用腿肌出力站起，切勿弯腰，以防伤及背部和腰。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      61、<span style="color:#990000">[判断题]</span> <strong>电气设备和大型仪器须接地良好，对电线老化等隐患要定期检查并及时排除。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      62、<span style="color:#990000">[判断题]</span> <strong>实验室应对仪器设备加强维护保养,定期校验和检修。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      63、<span style="color:#990000">[判断题]</span> <strong><p>电离辐射（放射性）的警告标识是:&nbsp;<br />
<img height="120" alt="" width="126" src="/attachments/2009-09/07-1251959248-1699.jpg" /></p></strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      64、<span style="color:#990000">[判断题]</span> <strong>涉辐人员必须持有辐射安全与防护培训合格证书，并佩带个人剂量计进行实验。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      65、<span style="color:#990000">[判断题]</span> <strong>使用电子门禁的大楼和实验室，应对各类人员设置相应的级别，对于门禁卡丢失、人员调动或离校等情况应及时采取措施，办理报失或移交手续。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      66、<span style="color:#990000">[判断题]</span> <strong>电炉、烘箱等用电设备在使用中，使用人员不得离开。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      67、<span style="color:#990000">[判断题]</span> <strong>实验室的接线板远离可能有水的位置和高温环境。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      68、<span style="color:#990000">[判断题]</span> <strong>夏季天气热时可以在实验室内穿露有脚趾的鞋。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  错误              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      69、<span style="color:#990000">[判断题]</span> <strong>一些低毒、无毒的实验废液可以不经处理，直接由下水道排放。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  错误              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      70、<span style="color:#990000">[判断题]</span> <strong>不准在车间打闹，不准随意攀登吊车、墙梯或者其它设备，不准在吊车吊运物体运行线上行走或停留。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      71、<span style="color:#990000">[单选题]</span> <strong>化学强腐蚀烫、烧伤事故发生后，应     ，保持创伤面的洁净以待医务人员治疗。或用适合于消除这类化学药品的特种溶剂、溶液仔细洗涤烫、烧伤面。</strong> （分值1.0）<br/>
      <ul><li>A．迅速用大量清水冲洗干净皮肤<br />
B．迅速解脱伤者被污染衣服，及时用大量清水冲洗干净皮肤<br />
C．迅速解脱伤者被污染衣服</li></ul>              你未作答
            标准答案：
                  B
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      72、<span style="color:#990000">[单选题]</span> <strong>在实验中，以下哪种做法是错误的？</strong> （分值1.0）<br/>
      <ul><li>A．一旦浓硫酸落在人体身上时，用4.5%乙酸或1.5%左右的盐酸中和洗涤<br />
B．一旦浓硫酸落在人体身上时，以弱碱（2%碳酸钠）或肥皂液中和洗涤<br />
C．一旦碱液落在皮肤上时，用4.5%乙酸或1.5%左右的盐酸中和洗涤</li></ul>              你未作答
            标准答案：
                  A
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      73、<span style="color:#990000">[单选题]</span> <strong>实验中溅入口中已下咽的强碱，先饮用大量水，再服用：</strong> （分值1.0）<br/>
      <ul><li>A．氢氧化铝膏，鸡蛋白<br />
B．乙酸果汁，鸡蛋白<br />
C．硫酸铜溶液（31g溶于一杯水中）催吐</li></ul>              你未作答
            标准答案：
                  B
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      74、<span style="color:#990000">[单选题]</span> <strong>在使用设备时，如果发现设备工作异常，怎么办？</strong> （分值1.0）<br/>
      <ul><li>A. 停机并报告相关负责人员  <br />
B. 关机走人<br />
C. 继续使用，注意观察<br />
D. 停机自行维修</li></ul>              你未作答
            标准答案：
                  A
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      75、<span style="color:#990000">[单选题]</span> <strong>师生进入实验室工作，一定要搞清楚   等位置，有异常情况，要关闭相应的总开关。</strong> （分值1.0）<br/>
      <ul><li>A．日光灯开关、水槽、通风橱<br />
B．电源总开关、水源总开关<br />
C．通风设备开关、多媒体开关、计算机开关</li></ul>              你未作答
            标准答案：
                  B
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      76、<span style="color:#990000">[单选题]</span> <strong>在实验内容设计过程中，要尽量选择什么物品做实验？</strong> （分值1.0）<br/>
      <ul><li>A．无公害、无毒或低毒的物品<br />
B．实验的残液、残渣较多的物品<br />
C．实验的残液、残渣不可回收的物品</li></ul>              你未作答
            标准答案：
                  A
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      77、<span style="color:#990000">[单选题]</span> <strong>根据卫生部规定，人间传染的病原微生物按危害程度可分为四类，其中哪类危害程度最高？</strong> （分值1.0）<br/>
      <ul><li>A. 第一类<br />
B. 第二类<br />
C. 第三类<br />
D. 第四类</li></ul>              你未作答
            标准答案：
                  A
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      78、<span style="color:#990000">[单选题]</span> <strong>根据农业部规定，动物病原微生物按危害程度可分为四类，其中哪类危害程度最高？</strong> （分值1.0）<br/>
      <ul><li>A. 第一类<br />
B. 第二类<br />
C. 第三类<br />
D. 第四类</li></ul>              你未作答
            标准答案：
                  A
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      79、<span style="color:#990000">[单选题]</span> <strong>目前实验动物中，比较严重的人畜共患病是什么？</strong> （分值1.0）<br/>
      <ul><li>A. 兔瘟病  <br />
B. 犬瘟热  <br />
C. 出血热病  <br />
D. 猴B病毒病</li></ul>              你未作答
            标准答案：
                  C
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      80、<span style="color:#990000">[单选题]</span> <strong>一般准备活动主要是一些全身性身体练习，主要包括         、踢腿、弯腰等。</strong> （分值1.0）<br/>
      <ul><li>A. 慢走      <br />
B. 俯卧撑      <br />
C. 慢跑   <br />
D. 游戏</li></ul>              你未作答
            标准答案：
                  C
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      81、<span style="color:#990000">[单选题]</span> <strong>干粉灭火器适用于：</strong> （分值1.0）<br/>
      <ul><li>A. 电器起火<br />
B. 可燃气体起火<br />
C. 有机溶剂起火<br />
D．以上都是</li></ul>              你未作答
            标准答案：
                  D
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      82、<span style="color:#990000">[单选题]</span> <strong>下列哪项不是影响混合物爆炸极限的因素?</strong> （分值1.0）<br/>
      <ul><li>A. 混合物的温度、压力<br />
B. 混合物的多少<br />
C. 混合物的含氧量 <br />
D. 容器的大小</li></ul>              你未作答
            标准答案：
                  B
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      83、<span style="color:#990000">[单选题]</span> <strong>下列选项中属于防爆的措施有：</strong> （分值1.0）<br/>
      <ul><li>A. 防止形成爆炸性混合物的化学品泄漏<br />
B. 控制可燃物形成爆炸性混合物                      <br />
C. 消除火源、安装检测和报警装置<br />
D. 以上都是</li></ul>              你未作答
            标准答案：
                  D
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      84、<span style="color:#990000">[单选题]</span> <strong>在火灾逃生方法中，以下不正确的是：</strong> （分值1.0）<br/>
      <ul><li>A.用湿毛巾捂着嘴巴和鼻子?????? <br />
B.弯着身子快速跑到安全地点<br />
C.躲在床底下，等待消防人员救援? <br />
D.马上从最近的消防通道跑到安全地点。</li></ul>              你未作答
            标准答案：
                  C
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      85、<span style="color:#990000">[单选题]</span> <strong>实验大楼因出现火情发生浓烟已穿入实验室内时，以下哪种行为是正确的？</strong> （分值1.0）<br/>
      <ul><li><br />
A．沿地面匍匐前进，当逃到门口时，不要站立开门<br />
B．打开实验室门后不用随手关门<br />
C．从楼上向楼下外逃时可以乘电梯</li></ul>              你未作答
            标准答案：
                  A
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      86、<span style="color:#990000">[单选题]</span> <strong>被电击的人能否获救，关键在于：</strong> （分值1.0）<br/>
      <ul><li>A. 触电的方式              <br />
B. 能否尽快脱离电源和施行紧急救护 <br />
C. 触电电压的高低 <br />
D. 人体电阻</li></ul>              你未作答
            标准答案：
                  B
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      87、<span style="color:#990000">[单选题]</span> <strong>如果触电者伤势严重，呼吸停止或心脏停止跳动，应先竭力采用胸外心脏挤压和   方法进行施救。</strong> （分值1.0）<br/>
      <ul><li>A．按摩                 <br />
B．点穴                 <br />
C. 人工呼吸<br />
D. 送医院</li></ul>              你未作答
            标准答案：
                  C
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      88、<span style="color:#990000">[单选题]</span> <strong>以下符合急救与防护“四先四后”原则的是：</strong> （分值1.0）<br/>
      <ul><li>A．先抢后救                  <br />
B. 先轻后重<br />
C．先缓后急                  <br />
D. 先病后伤</li></ul>              你未作答
            标准答案：
                  A
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      89、<span style="color:#990000">[单选题]</span> <strong>有机物或能与水发生剧烈化学反应的药品着火，应用       ，以免扑救不当造成更大损害。</strong> （分值1.0）<br/>
      <ul><li>A．其他有机物灭火<br />
B．自来水灭火<br />
C．灭火器或沙子扑灭</li></ul>              你未作答
            标准答案：
                  C
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      90、<span style="color:#990000">[单选题]</span> <strong>药品中毒的途径有哪些？</strong> （分值1.0）<br/>
      <ul><li>A. 呼吸器官吸入    <br />
B. 由皮肤渗入      <br />
C. 吞入<br />
D. 以上都是</li></ul>              你未作答
            标准答案：
                  D
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      91、<span style="color:#990000">[单选题]</span> <strong>CO是什么味？</strong> （分值1.0）<br/>
      <ul><li>A. 酸味  <br />
B. 烂苹果味  <br />
C. 无味<br />
D. 臭鸡蛋味</li></ul>              你未作答
            标准答案：
                  C
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      92、<span style="color:#990000">[单选题]</span> <strong>以下对放射性垃圾的安全管理不正确的是：</strong> （分值1.0）<br/>
      <ul><li>A. 允许非放射性垃圾混入放射性垃圾<br />
B. 将放射性垃圾放入专用容器收集、包装、储存，由专业部门统一回收处理<br />
C. 严禁放射性垃圾放入非放射性垃圾<br />
D. 放射性垃圾和非放射性垃圾必须分开放置</li></ul>              你未作答
            标准答案：
                  A
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      93、<span style="color:#990000">[单选题]</span> <strong>随手使用的手纸、饮料瓶等垃圾应该如何处理？</strong> （分值1.0）<br/>
      <ul><li>A．扔桌子上<br />
B．扔地上<br />
C．交给老师<br />
D. 扔垃圾桶</li></ul>              你未作答
            标准答案：
                  D
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      94、<span style="color:#990000">[单选题]</span> <strong>实验室、办公室等用电场所如需增加电器设备，以下说法正确的是？</strong> （分值1.0）<br/>
      <ul><li>A．老师自行改装<br />
B．须经学校有关部门批准，并由学校指派电工安装<br />
C．学生可以私自改接</li></ul>              你未作答
            标准答案：
                  B
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      95、<span style="color:#990000">[单选题]</span> <strong>生物实验中的一次性手套及沾染EB致癌物质的物品，应：</strong> （分值1.0）<br/>
      <ul><li><br />
A．丢弃在普通垃圾箱内<br />
B．统一收集和处理<br />
C．随意放在实验室</li></ul>              你未作答
            标准答案：
                  B
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      96、<span style="color:#990000">[单选题]</span> <strong>由于行为人的过失引起火灾，造成严重后果，危害公共安全的行为，构成：</strong> （分值1.0）<br/>
      <ul><li>A. 纵火罪<br />
B. 失火罪<br />
C. 玩忽职守罪<br />
D. 重大责任事故罪</li></ul>              你未作答
            标准答案：
                  B
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      97、<span style="color:#990000">[单选题]</span> <strong>雷电放电具有什么特点？</strong> （分值1.0）<br/>
      <ul><li>A. 电流大，电压高      <br />
B．电流小，电压高      <br />
C．电流大，电压低<br />
D. 电磁波辐射</li></ul>              你未作答
            标准答案：
                  A
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      98、<span style="color:#990000">[单选题]</span> <strong>一般居民住宅、办公场所，若以防止触电为主要目的时，应选用漏电动作电流为多少的漏电保护开关？</strong> （分值1.0）<br/>
      <ul><li>A. 6 mA      <br />
B. 15mA      <br />
C. 30mA<br />
D. 50mA</li></ul>              你未作答
            标准答案：
                  C
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      99、<span style="color:#990000">[单选题]</span> <strong>进行照明设施的接电操作，应采取的防触电措施为：</strong> （分值1.0）<br/>
      <ul><li>A. 湿手操作      <br />
B. 切断电源         <br />
C. 站在金属登子或梯子上 <br />
D. 戴上手套</li></ul>              你未作答
            标准答案：
                  B
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      100、<span style="color:#990000">[单选题]</span> <strong>引起电器线路火灾的原因是：</strong> （分值1.0）<br/>
      <ul><li>A. 短路<br />
B. 电火花<br />
C. 负荷过载<br />
D．以上都是</li></ul>              你未作答
            标准答案：
                  D
              
              </div>
                      
              <div class="nav">
                   <ul>
                	<li><img src="/template/images/arrow1_085.gif" /> <a href="/">返回考试首页</a></li>
                   </ul>
                </div>   
              
          </div>
          
<div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      1、<span style="color:#990000">[判断题]</span> <strong>重复接地是指零线上的一处或多处通过接地装置与大地再连接，可提高线路的安全性。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      2、<span style="color:#990000">[判断题]</span> <strong>消除管线上的静电主要是做好屏蔽。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  错误              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      3、<span style="color:#990000">[判断题]</span> <strong>保险丝和空气开关可以有效地防止电气火灾。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  错误              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      4、<span style="color:#990000">[判断题]</span> <strong>金属材料可以很好地屏蔽低频磁场。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  错误              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      5、<span style="color:#990000">[判断题]</span> <strong>在使用手电钻、电砂轮等手持电动工具时，为保证安全，应该装设漏电保护器。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      6、<span style="color:#990000">[判断题]</span> <strong>身边有人严重触电，应当首先切断电源，然后进行紧急抢救如人工呼吸，并立即拨打急救电话120。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      7、<span style="color:#990000">[判断题]</span> <strong>在有爆炸和火灾危险场所使用手持式或移动式电动工具时，必须采用有防爆措施的电动工具。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      8、<span style="color:#990000">[判断题]</span> <strong>在进行电子线路板焊接后的剪脚工序时，剪脚面应背离身体特别是脸部，防止被剪下引脚弹伤。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      9、<span style="color:#990000">[判断题]</span> <strong>电击（触电）通常指因为人体接触带电的线路或设备而受到伤害的事故。为了避免电击（触电）事故的发生，设备须可靠接地和人体对地绝缘。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      10、<span style="color:#990000">[判断题]</span> <strong>静电有三大特点：一是电压高；二是静电感应突出；三是尖端放电现象严重。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      11、<span style="color:#990000">[判断题]</span> <strong>电流对人体的伤害有两种类型：即电击和电伤。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      12、<span style="color:#990000">[判断题]</span> <strong>短路是指电气线路中相线与相线，相线与零线或大地，在未通过负载或电阻很小的情况下相碰，造成电气回路中电流剧增的现象。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      13、<span style="color:#990000">[判断题]</span> <strong>电分强电和弱电，弱电开关等元件不能用在强电电路。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      14、<span style="color:#990000">[判断题]</span> <strong>用电安全的基本要素有：电气绝缘良好、保证安全距离、线路与插座容量与设备功率相适宜、不使用三无产品。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      15、<span style="color:#990000">[判断题]</span> <strong>高压实验中的安全距离：10kV是0.7m；66kV是1.5m；220kV是3m。  </strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      16、<span style="color:#990000">[判断题]</span> <strong>50毫安的工频电流就可以使人遭到致命电击。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      17、<span style="color:#990000">[判断题]</span> <strong>万用表电阻档可测量绝缘电阻。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  错误              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      18、<span style="color:#990000">[判断题]</span> <strong>电路谐振时，电容的电压可以是电源电压的几倍。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      19、<span style="color:#990000">[判断题]</span> <strong>人体触电，双手触电致死比单手触电致死的概率要大得多。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      20、<span style="color:#990000">[判断题]</span> <strong>静电可以引起爆炸、电气绝缘和电子元器件击穿。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      21、<span style="color:#990000">[判断题]</span> <strong>地线和零线的作用相同。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  错误              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      22、<span style="color:#990000">[判断题]</span> <strong>短路会使短路处甚至整个电路过热，从而导致线路的绝缘层燃烧，引发火灾。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      23、<span style="color:#990000">[判断题]</span> <strong>各种电源是否有电，可用试电笔检验。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  错误              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      24、<span style="color:#990000">[判断题]</span> <strong>漏电保护器对两相触电（人体双手触及两相电源），不起保护作用。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      25、<span style="color:#990000">[判断题]</span> <strong>漏电保护器既可用来保护人身安全，还可用来对低压系统或设备的绝缘状况起到监督作用；漏电保护器安装点以后的线路应是对地绝缘良好。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      26、<span style="color:#990000">[判断题]</span> <strong>电气检修时,应在配电箱或开关处悬挂“禁止合闸，有人工作”的标示牌。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      27、<span style="color:#990000">[判断题]</span> <strong>布线时,强、弱电可以合用同一电缆管线。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  错误              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      28、<span style="color:#990000">[判断题]</span> <strong>使用钳形电流表时，应注意钳形电流表的量程。测量时戴绝缘手套，站在绝缘垫上，不得触及其它设备，以防短路或接地。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      29、<span style="color:#990000">[判断题]</span> <strong>在潮湿或高温或有导电灰尘的场所，实验时应该降低电压供电。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      30、<span style="color:#990000">[判断题]</span> <strong>电路保险丝熔断，短期内可以用铜丝或铁丝代替。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  错误              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      31、<span style="color:#990000">[判断题]</span> <strong>连接电气设备的开关需安装在火线上。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      32、<span style="color:#990000">[判断题]</span> <strong>打开含有高压变压器或电容器的电子仪器的盖子是危险的。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      33、<span style="color:#990000">[判断题]</span> <strong>电动工具的电源引线必须保证接地可靠。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      34、<span style="color:#990000">[判断题]</span> <strong>接电路元器件时，主要应关注元器件的耐压和能承受的功率。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      35、<span style="color:#990000">[判断题]</span> <strong>电磁式电流互感器在使用中付边不许开路，电压互感器在使用中付边不许短路。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      36、<span style="color:#990000">[判断题]</span> <strong>实验室禁止私拉乱接电线，实验过程中自制非标设备时，应报请实验室管理人员批准，然后请电气专业人员按照标准安全的连接。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      37、<span style="color:#990000">[判断题]</span> <strong>只要接线板质量符合要求，就可以随意串联很多个，不影响使用。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  错误              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      38、<span style="color:#990000">[判断题]</span> <strong>在充满可燃气体的环境中，可以使用手动电动工具。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  错误              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      39、<span style="color:#990000">[判断题]</span> <strong>在易燃、易爆、易灼烧及有静电发生的场所，可以使用化纤防护用品。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  错误              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      40、<span style="color:#990000">[判断题]</span> <strong>电动工具应定期检修。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      41、<span style="color:#990000">[判断题]</span> <strong>连接在接线板上的用电总负荷不能超过接线板的最大容量。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      42、<span style="color:#990000">[判断题]</span> <strong>在电气类开放性实验或科研实验室，必须二人以上方可开展实验。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      43、<span style="color:#990000">[判断题]</span> <strong>为了防止触电可采用绝缘、防护、隔离等技术措施以保障安全。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      44、<span style="color:#990000">[判断题]</span> <strong>对容易产生静电的场所，要保持空气潮湿；工作人员要穿防静电的衣服和鞋靴。?</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      45、<span style="color:#990000">[单选题]</span> <strong>测量绝缘电阻可用：</strong> （分值1.0）<br/>
      <ul><li>A. 万用表<br />
B. 兆欧表<br />
C. 示波器<br />
D. 电笔</li></ul>              你未作答
            标准答案：
                  B
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      46、<span style="color:#990000">[单选题]</span> <strong>引发电气火灾的初始原因是:</strong> （分值1.0）<br/>
      <ul><li>A. 电源保险丝不起作用<br />
B. 带电改接电气线路<br />
C. 线路或设备过电流运行<br />
D. 没有保护性接零或接地</li></ul>              你未作答
            标准答案：
                  C
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      47、<span style="color:#990000">[单选题]</span> <strong>低压电笔一般适用于多少?V?以下的交流电压？</strong> （分值1.0）<br/>
      <ul><li>A. 220      <br />
B. 380         <br />
C. 500 <br />
D.  36</li></ul>              你未作答
            标准答案：
                  C
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      48、<span style="color:#990000">[单选题]</span> <strong>安装使用漏电保护器，是属于哪种安全技术措施? </strong> （分值1.0）<br/>
      <ul><li>A．基本安全措施        <br />
B．辅助安全措施         <br />
C．绝对安全措施 <br />
D. 应急安全措施</li></ul>              你未作答
            标准答案：
                  A
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      49、<span style="color:#990000">[单选题]</span> <strong>漏电保护器可防止：</strong> （分值1.0）<br/>
      <ul><li>A. 触电事故                <br />
B．电压波动        <br />
C．电流过大<br />
D. 双手触电事故</li></ul>              你未作答
            标准答案：
                  A
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      50、<span style="color:#990000">[单选题]</span> <strong>单相三芯线电缆中的红线代表什么？</strong> （分值1.0）<br/>
      <ul><li>A．零线             <br />
B．火线              <br />
C．地线 <br />
D. 不明确</li></ul>              你未作答
            标准答案：
                  B
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      51、<span style="color:#990000">[单选题]</span> <strong>工作地点相对湿度大于?75%?时，属于什么环境？</strong> （分值1.0）<br/>
      <ul><li>A. 危险、易触电     <br />
B. 不危险       <br />
C. 一般 <br />
D. 特殊</li></ul>              你未作答
            标准答案：
                  A
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      52、<span style="color:#990000">[单选题]</span> <strong>下列有关使用漏电保护器的说法，哪种是正确的?                   </strong> （分值1.0）<br/>
      <ul><li>A. 漏电保护器既可用来保护人身安全，还可用来对低压系统或设备的对地绝缘状况起到监督作用<br />
B．漏电保护器安装点以后的线路不可对地绝缘<br />
C．漏电保护器在日常使用中不可在通电状态下按动实验按钮来检验其是否可靠<br />
D. 对两相触电起保护作用</li></ul>              你未作答
            标准答案：
                  A
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      53、<span style="color:#990000">[单选题]</span> <strong>安全电压是指保证不会对人体产生致命危险的电压值，工业中使用的安全电压是多少以下？</strong> （分值1.0）<br/>
      <ul><li>A. 25V<br />
B. 36V<br />
C. 50V<br />
D. 110V</li></ul>              你未作答
            标准答案：
                  B
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      54、<span style="color:#990000">[单选题]</span> <strong>为了减少电击（触电）事故对人体的损伤，经常用到电流型漏电保护开关，其保护指标设置为≤30mAS。请从下列选项中选择其正确含义。</strong> （分值1.0）<br/>
      <ul><li>A. 流经人体的电流（以毫安为单位）和时间（以秒为单位）的乘积小于30。例如电流为30mA则持续的时间必须小于1秒<br />
B. 流经人体的电流必须小于30毫安<br />
C. 流经人体电流的持续时间必须小于1秒<br />
D. 流经人体的电流必须小于30微安</li></ul>              你未作答
            标准答案：
                  A
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      55、<span style="color:#990000">[单选题]</span> <strong>下列哪些是预防电气火灾的基本措施？</strong> （分值1.0）<br/>
      <ul><li>A. 禁止非电工改接电气线路，禁止乱拉临时用电线路        <br />
B. 做电气类实验时应该2人及以上在场<br />
C. 从工作现场清除易燃易爆材料<br />
D. 以上都是</li></ul>              你未作答
            标准答案：
                  D
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      56、<span style="color:#990000">[单选题]</span> <strong>自耦电源变压器的输出端指示电压为零时，表示：</strong> （分值1.0）<br/>
      <ul><li>A. 是安全的<br />
B. 不带电<br />
C. 未必是安全的（如果输入端火线和零线未按要求接，变压器付边会有高压）</li></ul>              你未作答
            标准答案：
                  C
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      57、<span style="color:#990000">[单选题]</span> <strong>交流电路断电后，内部的电容可能会：</strong> （分值1.0）<br/>
      <ul><li>A. 电死人<br />
B. 用仪表测量电容值时，会损坏仪表<br />
C. 有高电压    <br />
D. 以上都是</li></ul>              你未作答
            标准答案：
                  D
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      58、<span style="color:#990000">[单选题]</span> <strong>引发电气火灾的初始原因：</strong> （分值1.0）<br/>
      <ul><li>A. 电源保险丝不起作用<br />
B. 带电改接电气线路<br />
C. 绝缘老化或破坏<br />
D. 室内湿度</li></ul>              你未作答
            标准答案：
                  C
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      59、<span style="color:#990000">[单选题]</span> <strong>影响电流对人体伤害程度的主要因素是什么？</strong> （分值1.0）<br/>
      <ul><li>A. 电流的大小                <br />
B. 触电电流经人体的途径     <br />
C. 电流的频率、人体电阻<br />
D. 以上都是</li></ul>              你未作答
            标准答案：
                  D
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      60、<span style="color:#990000">[单选题]</span> <strong>动力配电线五线制U、V、W、零线、地线的色标分别为：</strong> （分值1.0）<br/>
      <ul><li>A. 蓝、双色线、黄、绿、红<br />
B. 黄、绿、红、蓝、双色线<br />
C. 双色线、黄、绿、红、蓝<br />
D. 红、蓝、双色线、黄、绿</li></ul>              你未作答
            标准答案：
                  B
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      61、<span style="color:#990000">[单选题]</span> <strong>长期在高频电磁场作用下，操作者会有什么不良反应? </strong> （分值1.0）<br/>
      <ul><li>A. 呼吸困难                <br />
B．神经失常             <br />
C．疲劳无力 <br />
D. 心跳减慢     </li></ul>              你未作答
            标准答案：
                  C
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      62、<span style="color:#990000">[单选题]</span> <strong>三相电闸闭合后或三相空气开关闭合后，三相电机嗡嗡响、不转或转速很慢。为什么？</strong> （分值1.0）<br/>
      <ul><li>A．短路      <br />
B. 开路      <br />
C. 缺相 <br />
D. 三相电源对称</li></ul>              你未作答
            标准答案：
                  C
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      63、<span style="color:#990000">[单选题]</span> <strong>下列哪种灭火器不适于扑灭电器火灾?</strong> （分值1.0）<br/>
      <ul><li>A．二氧化碳灭火器          <br />
B．干粉灭火器           <br />
C．泡沫灭火器</li></ul>              你未作答
            标准答案：
                  C
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      64、<span style="color:#990000">[单选题]</span> <strong>电源电压高于电容耐压时，会引起: </strong> （分值1.0）<br/>
      <ul><li>A. 电容短路<br />
B. 电容发热<br />
C. 电容爆裂而伤害到人<br />
D. 电容不会爆裂</li></ul>              你未作答
            标准答案：
                  C
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      65、<span style="color:#990000">[单选题]</span> <strong>实验时，电源变压器付边输出被短路，会出现什么现象，直至烧毁？</strong> （分值1.0）<br/>
      <ul><li>A. 电源变压器有异味<br />
B. 电源变压器冒烟<br />
C. 电源变压器发热<br />
D. 以上都是</li></ul>              你未作答
            标准答案：
                  D
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      66、<span style="color:#990000">[单选题]</span> <strong>在有电阻、电容、电感的电路中，电源电压是几十伏，电容或电感的电压可以是：</strong> （分值1.0）<br/>
      <ul><li>A. 几十伏<br />
B. 不超过电源电压<br />
C. 超过百伏    <br />
D. 不会触死人                                 </li></ul>              你未作答
            标准答案：
                  C
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      67、<span style="color:#990000">[单选题]</span> <strong>电线接地时，人体距离接地点越近，跨步电压越高；距离越远，跨步电压越低。一般情况下距离接地体多少，跨步电压可看成是零？</strong> （分值1.0）<br/>
      <ul><li>A. 10m 以内     <br />
B. 20m 以外      <br />
C. 30m 以外 <br />
D. 50m 以外</li></ul>              你未作答
            标准答案：
                  B
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      68、<span style="color:#990000">[单选题]</span> <strong>使用电烙铁应注意：</strong> （分值1.0）<br/>
      <ul><li>A. 不能乱甩焊锡<br />
B. 及时放回烙铁架，用完及时切断电源<br />
C. 周围不得放置易燃物品<br />
D. 以上都是</li></ul>              你未作答
            标准答案：
                  D
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      69、<span style="color:#990000">[单选题]</span> <strong>预防电击（触电）的一条重要措施是用电设备的金属外壳要有效接地。请从下列选项中选择可靠的接地点：</strong> （分值1.0）<br/>
      <ul><li>A. 单相供电的2根线分别称为火线和地线，选择其中的地线接地<br />
B. 三相供电中的中性点电压应该为零，可以选择这个中性点来接地<br />
C. 专门埋设地下、保证接地电阻很小专用地线<br />
D. 实验室内的自来水管（暖气管）是埋设于地下的金属管相连的，可用来接地</li></ul>              你未作答
            标准答案：
                  C
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      70、<span style="color:#990000">[单选题]</span> <strong>使用电气设备时，由于维护不及时，当什么进入时可导致短路事故？</strong> （分值1.0）<br/>
      <ul><li>A．导电粉尘或纤维        <br />
B．强光辐射          <br />
C．高温环境 <br />
D. 潮气</li></ul>              你未作答
            标准答案：
                  A
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      71、<span style="color:#990000">[单选题]</span> <strong>设备或线路的确认无电，应以什么指示作为根据？ </strong> （分值1.0）<br/>
      <ul><li>A. 电压表     <br />
B. 正常的验电工具      <br />
C. 断开信号<br />
D. 电流表</li></ul>              你未作答
            标准答案：
                  B
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      72、<span style="color:#990000">[单选题]</span> <strong>移动式电动工具及其开关板（箱）的电源线必须采用：</strong> （分值1.0）<br/>
      <ul><li>A. 双层塑料铜芯绝缘导线<br />
B. 双股铜芯塑料软线 <br />
C. 铜芯橡皮绝缘护套或铜芯聚氯乙烯绝缘护套软线 <br />
D. 单股铜芯塑料软线</li></ul>              你未作答
            标准答案：
                  C
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      73、<span style="color:#990000">[单选题]</span> <strong>长期搁置不用的手持电动工具，在使用前必须测量绝缘电阻，要求手持电动工具带电部分与外壳之间绝缘电阻不低于多少MΩ？</strong> （分值1.0）<br/>
      <ul><li>A. 2     <br />
B. 0.5       <br />
C. 1 <br />
D. 10</li></ul>              你未作答
            标准答案：
                  B
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      74、<span style="color:#990000">[单选题]</span> <strong>对于高压电容器，实验结束后或闲置时，如何处理最合适？</strong> （分值1.0）<br/>
      <ul><li>     <br />
A. 电极接地 <br />
B. 双电极短接（串接合适电阻进行放电）<br />
C. 双电极接地 <br />
D. 不处理</li></ul>              你未作答
            标准答案：
                  B
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      75、<span style="color:#990000">[单选题]</span> <strong>以下有关实验室用电的注意事项中，不正确的是：</strong> （分值1.0）<br/>
      <ul><li>A. 实验前先检查用电设备，再接通电源；实验结束后，先关仪器设备，再关闭电源<br />
B. 工作人员离开实验室或遇突然断电，应关闭电源，尤其要关闭加热电器的电源开关<br />
C. 电源或电器设备的保险丝烧断后，可以用其它金属导线代替<br />
D. 不得将供电线任意放在通道上，以免因绝缘破损造成短路</li></ul>              你未作答
            标准答案：
                  C
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      76、<span style="color:#990000">[单选题]</span> <strong>停电检修时，在一经合闸即可送电到工作地点的开关或刀闸的操作把手上，应悬挂如下哪种标示牌?</strong> （分值1.0）<br/>
      <ul><li>A.  ""在此工作”   <br />
B．“止步，高压危险”  <br />
C．“禁止合闸，有人工作”<br />
D. “今日休息”</li></ul>              你未作答
            标准答案：
                  C
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      77、<span style="color:#990000">[单选题]</span> <strong>使用手持电动工具时，下列哪个措施不正确? </strong> （分值1.0）<br/>
      <ul><li>A．使用静电防护毯<br />
B．带防护手套 <br />
C．使用漏电保护器<br />
D. 穿绝缘鞋</li></ul>              你未作答
            标准答案：
                  A
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      78、<span style="color:#990000">[单选题]</span> <strong>任何电气设备在未验明无电之前，一律认为：</strong> （分值1.0）<br/>
      <ul><li>A．无电       <br />
B．也许有电                <br />
C．有电<br />
D. 也许无电</li></ul>              你未作答
            标准答案：
                  C
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      79、<span style="color:#990000">[单选题]</span> <strong>电路实验中，下列哪种操作是错误的？</strong> （分值1.0）<br/>
      <ul><li>A．电压源不能短路       <br />
B．电流源不能短路         <br />
C．电流源能短路 <br />
D. 上述操作都是正确的</li></ul>              你未作答
            标准答案：
                  B
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      80、<span style="color:#990000">[单选题]</span> <strong>静电的电量虽然不大，但其放电时产生的静电火花有可能引起爆炸和火灾，比较常见的是放电时瞬间的电流造成精密实验仪器损坏，不正确的预防措施有:</strong> （分值1.0）<br/>
      <ul><li>A. 适当提高工作场所的湿度<br />
B. 进行特殊危险实验时，操作人员应先接触设置在安全区内的金属接地棒，以消除人体电位<br />
C. 在易产生静电的场所梳理头发<br />
D. 计算机进行维护时，使用防静电毯</li></ul>              你未作答
            标准答案：
                  C
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      81、<span style="color:#990000">[单选题]</span> <strong>万用表使用完后，应将切换旋钮放在:</strong> （分值1.0）<br/>
      <ul><li>A. 电阻档<br />
B. 直流电压档<br />
C. 交流电压最高档<br />
D. 电流量档</li></ul>              你未作答
            标准答案：
                  C
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      82、<span style="color:#990000">[单选题]</span> <strong>因实验需要拉接电源线,下列哪种说法是正确的？</strong> （分值1.0）<br/>
      <ul><li>A. 不得任意放置于通道上，以免因绝缘破损造成短路或影响通行<br />
B. 插座不足时，可连续串接<br />
C. 插座不足时，可连续分接<br />
D. 不考虑负荷容量</li></ul>              你未作答
            标准答案：
                  A
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      83、<span style="color:#990000">[单选题]</span> <strong>电分强电和弱电。下列说法正确的是：</strong> （分值1.0）<br/>
      <ul><li>A. 强电和弱电开关等元件可通用                                      <br />
B. 弱电开关等元件不可用在强电电路                            <br />
C. 开关不分强弱<br />
D. 弱电开关等元件可用在强电电路</li></ul>              你未作答
            标准答案：
                  B
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      84、<span style="color:#990000">[单选题]</span> <strong>在需要带电操作的低电压电路实验时，下列哪种是正确的？                        
</strong> （分值1.0）<br/>
      <ul><li>A. 双手操作比单手操作安全           <br />
B. 单手操作比双手操作安全   <br />
C. 单手操作和双手操作一样安全<br />
D. 操作与空气湿度有关</li></ul>              你未作答
            标准答案：
                  B
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      85、<span style="color:#990000">[单选题]</span> <strong>强电实验时，实验人员必须几人以上？</strong> （分值1.0）<br/>
      <ul><li>A. 1        <br />
B. 2       <br />
C. 3  <br />
D. 4</li></ul>              你未作答
            标准答案：
                  B
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      86、<span style="color:#990000">[单选题]</span> <strong>雷电由于瞬间的强大电流释放巨大能量，不仅会伤及人员，还会损坏设备，甚至引起火灾。请在下列选项中选择室内防止雷电灾害的最主要的一项措施。</strong> （分值1.0）<br/>
      <ul><li>A. 在较高建筑的顶端及露天的配电设施要装避雷装置<br />
B. 雷雨时不使用计算机上网，而且尽可能关闭机器，拔掉电   源线和网线<br />
C. 雷雨发生时不使用手机<br />
D. 不使用电烙铁</li></ul>              你未作答
            标准答案：
                  A
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      87、<span style="color:#990000">[单选题]</span> <strong>如果工作场所潮湿，为避免触电，使用手持电动工具的人应：</strong> （分值1.0）<br/>
      <ul><li>A．站在铁板上操作               <br />
B．站在绝缘胶板上操作  <br />
C．穿防静电鞋操作 <br />
D. 戴上安全帽</li></ul>              你未作答
            标准答案：
                  B
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      88、<span style="color:#990000">[单选题]</span> <strong>在进行电子线路板焊接后的剪脚工序时应：</strong> （分值1.0）<br/>
      <ul><li>A．戴上防护眼镜       <br />
B．戴上护耳器        <br />
C．戴上安全帽 <br />
D. 戴上手套</li></ul>              你未作答
            标准答案：
                  A
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      89、<span style="color:#990000">[单选题]</span> <strong>电气设备的外壳应有什么防护措施? </strong> （分值1.0）<br/>
      <ul><li>A. 无        <br />
B．保护性接地          <br />
C．防锈漆<br />
D. 绝缘</li></ul>              你未作答
            标准答案：
                  B
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      90、<span style="color:#990000">[单选题]</span> <strong>为防止静电火花引起事故，凡是用来加工、贮存、运输各种易燃气、液、粉体的金属设备、非导电材料都必须：</strong> （分值1.0）<br/>
      <ul><li>A. 有足够大的电阻    <br />
B. 有足够小的电阻     <br />
C. 可靠接地<br />
D. 可靠绝缘</li></ul>              你未作答
            标准答案：
                  C
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      91、<span style="color:#990000">[单选题]</span> <strong>摩擦是产生静电的一种主要原因，尤其在干燥的环境中，人体的活动和物体的移动都会产生很强的静电。静电在突然释放的时会对人体或设备造成损伤，以下哪种是防止静电事故的主要办法。</strong> （分值1.0）<br/>
      <ul><li>A. 人体接触对静电敏感设备时提前释放自己身体中积累的电荷，例如带静电防护手环、使用静电防护毯<br />
B. 用电设备都良好接地<br />
C. 保证电路良好的绝缘<br />
D. 在易产生静电的场所梳理头发</li></ul>              你未作答
            标准答案：
                  A
              
              </div>


<div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      1、<span style="color:#990000">[判断题]</span> <strong>有“严禁烟火”警示牌的大楼和实验室，可不必配 置必要的消防、冲淋、洗眼、报警和逃生设施和有明显标志。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  错误              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      2、<span style="color:#990000">[判断题]</span> <strong>灭火器按其移动形式可分为：手提式和推车式。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      3、<span style="color:#990000">[判断题]</span> <strong>不得堵塞实验室逃生通道。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      4、<span style="color:#990000">[判断题]</span> <strong>身上着火被熄灭后,应马上把粘在皮肤上的衣物脱下来。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  错误              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      5、<span style="color:#990000">[判断题]</span> <strong>电气设备着火，首先必须采取的措施是灭火。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  错误              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      6、<span style="color:#990000">[判断题]</span> <strong>实验室发生非火灾类事故，应立即报告单位负责人 和学校保卫处，设立警戒区并撤离无关人员，以减轻潜在危害。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      7、<span style="color:#990000">[判断题]</span> <strong>火灾发生后，受到火势威胁时，要当机立断披上浸湿的衣物、被褥等向安全出口方向冲去。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      8、<span style="color:#990000">[判断题]</span> <strong>万一发生了火灾，不管是否是电气方面引起的，首先要想办法迅速切断火灾范围内的电源。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      9、<span style="color:#990000">[判断题]</span> <strong>火灾发生后，穿过浓烟逃生时，必须尽量贴近地面，并用湿毛巾捂住口鼻。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      10、<span style="color:#990000">[判断题]</span> <strong>火灾对实验室构成的威胁最为严重，最为直接。应加强对火灾三要素（易燃物、助燃物、点火源）的控制。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      11、<span style="color:#990000">[判断题]</span> <strong>消防队在扑救火灾时，有权根据灭火的需要，拆除或者破损临近火灾现场的建筑。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      12、<span style="color:#990000">[判断题]</span> <strong>发现火灾时，单位或个人应该先自救，当自救无效、火越着越大时，再拨打火警电话119。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  错误              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      13、<span style="color:#990000">[判断题]</span> <strong>火灾发生后，当所有的逃生线路被大火封锁时，应立即退回室内，用手电筒、挥舞衣物、呼叫等方式向窗外发送求救 信号，等待救援。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      14、<span style="color:#990000">[判断题]</span> <strong>当电气设备发生火灾后，如果可能应当先断电后灭火。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      15、<span style="color:#990000">[判断题]</span> <strong>当发生火情时尽快沿着疏散指示标志和安全出口方向迅速离开火场。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      16、<span style="color:#990000">[判断题]</span> <strong>消防工作的方针是：“预防为主，防消结合”，实行消防安全责任制。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      17、<span style="color:#990000">[判断题]</span> <strong>大火封门无路可逃时，可用浸湿的被褥、衣物堵塞门缝，向门上泼水降温，以延缓火灾蔓延时间，呼叫待援。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      18、<span style="color:#990000">[判断题]</span> <strong>实验室灭火的方法要针对起因选用合适的方法。一般小火可用湿布、石棉布或沙子覆盖燃烧物即可灭火。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      19、<span style="color:#990000">[判断题]</span> <strong>所有的火灾刚开始时都是小火，随着火灾的发展输出的热量越大，火灾蔓延的速度和范围也愈大，所以扑灭初起火灾 最容易的。</strong> （分值1.0）<br/>
                    你未作答
            标准答案：
                  正确              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      20、<span style="color:#990000">[单选题]</span> <strong>室内消火栓应设在明显易于取用的地点并有明显标识。其栓口离地面高度为（）</strong> （分值1.0）<br/>
      <ul><li>A、0.5米<br />
B、1.1米<br />
C、1.5米<br />
D、2米</li></ul>              你未作答
            标准答案：
                  B
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      21、<span style="color:#990000">[单选题]</span> <strong>建筑物安全疏散设施不包括（）</strong> （分值1.0）<br/>
      <ul><li>A、安全出口<br />
B、疏散指示标志<br />
C、应急广播<br />
D、普通电梯</li></ul>              你未作答
            标准答案：
                  D
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      22、<span style="color:#990000">[单选题]</span> <strong>可燃助燃的腐蚀品的腐蚀性主要体现在三个方面，不包括下列那一个选项（）</strong> （分值1.0）<br/>
      <ul><li>A、对人体的伤害<br />
B、对动物的伤害<br />
C、对有机物的破坏<br />
D、对金属的腐蚀性</li></ul>              你未作答
            标准答案：
                  C
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      23、<span style="color:#990000">[单选题]</span> <strong>许多易燃固体严禁与酸、氧化剂接触。是因为它具有（）的危险特性</strong> （分值1.0）<br/>
      <ul><li>A、燃点低，易点燃<br />
B、遇酸、氧化剂易燃易爆<br />
C、本身或燃烧产物有毒<br />
D、自燃性</li></ul>              你未作答
            标准答案：
                  B
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      24、<span style="color:#990000">[单选题]</span> <strong>当单位灭火人员不能接近火场时，应根据着火对象及火灾现场实际，果断地在蔓延方向采取一些必要的堵截措施。下列那种措施不能阻止火势蔓延（）</strong> （分值1.0）<br/>
      <ul><li>A、关闭防火门<br />
B、设置水枪阵地<br />
C、降下防火卷帘<br />
D、打开防火门</li></ul>              你未作答
            标准答案：
                  D
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      25、<span style="color:#990000">[单选题]</span> <strong>下列关于身上着火的处置方法，错误的一种是（）</strong> （分值1.0）<br/>
      <ul><li>A、身上着火，着火人可就地倒下打滚，把身上的火焰压灭<br />
B、身上着火，应尽快脱掉衣帽，快速奔跑，把身上的火焰吹灭<br />
C、身上着火，在场的其他人员可向着火人身上浇水，把火扑灭<br />
D、身上着火，在场的其他人员可用湿麻袋、毯子等物把着火人包裹起来窒息灭火</li></ul>              你未作答
            标准答案：
                  B
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      26、<span style="color:#990000">[单选题]</span> <strong>公共娱乐场所安全出口的疏散门应（）</strong> （分值1.0）<br/>
      <ul><li>A、自由开启<br />
B、疏散方向开启<br />
C、疏散反方向开启<br />
D、关闭</li></ul>              你未作答
            标准答案：
                  B
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      27、<span style="color:#990000">[单选题]</span> <strong>消防工作要贯彻( )</strong> （分值1.0）<br/>
      <ul><li>A、逐级防火责任制<br />
B、预防为主，防消结合方针<br />
C、岗位安全责任制<br />
D、谁主管谁负责</li></ul>              你未作答
            标准答案：
                  B
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      28、<span style="color:#990000">[单选题]</span> <strong>一些固体可燃物在空气不流通、加热温度较低或含水分较高时就会（）</strong> （分值1.0）<br/>
      <ul><li>A、闪燃<br />
B、阴燃<br />
C、分解燃烧<br />
D、表面燃烧</li></ul>              你未作答
            标准答案：
                  B
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      29、<span style="color:#990000">[单选题]</span> <strong>液体的火灾危险性是根据液体的（）分类的</strong> （分值1.0）<br/>
      <ul><li>A、燃点<br />
B、自燃点<br />
C、闪点<br />
D、凝固点</li></ul>              你未作答
            标准答案：
                  C
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      30、<span style="color:#990000">[单选题]</span> <strong>在易燃易爆场所作业的人员不能穿戴( )</strong> （分值1.0）<br/>
      <ul><li>A、尼龙工作服<br />
B、棉布工作服<br />
C、防静电服<br />
D、耐高温鞋</li></ul>              你未作答
            标准答案：
                  A
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      31、<span style="color:#990000">[单选题]</span> <strong>消防安全重点单位应当按照灭火和应急疏散预案，至少（ ）进行一次演练，其他单位应当结合本单位实际，至少（ ）组织一次演练（）</strong> （分值1.0）<br/>
      <ul><li>A、每月；每季度<br />
B、每季度；每半年<br />
C、每半年；每年<br />
D、每半年；每季度</li></ul>              你未作答
            标准答案：
                  C
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      32、<span style="color:#990000">[单选题]</span> <strong>水能扑救（）火灾</strong> （分值1.0）<br/>
      <ul><li>A、石油、汽油<br />
B、熔化的铁水、钢水<br />
C、高压电器设备<br />
D、木材、纸张</li></ul>              你未作答
            标准答案：
                  D
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      33、<span style="color:#990000">[单选题]</span> <strong>违反消防法的规定，生产、储存、运输、销售或者使用、销毁易燃易爆危险物品的，责令停止违法行为，可以处警告、罚款或者（）</strong> （分值1.0）<br/>
      <ul><li>A、十五日以下拘留<br />
B、治安处罚<br />
C、行政处分<br />
D、其他</li></ul>              你未作答
            标准答案：
                  A
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      34、<span style="color:#990000">[单选题]</span> <strong>ABC干粉灭火器不能扑救( )火灾</strong> （分值1.0）<br/>
      <ul><li>A、金属物质<br />
B、固体物质<br />
C、液体物质<br />
D、气体物质</li></ul>              你未作答
            标准答案：
                  A
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      35、<span style="color:#990000">[单选题]</span> <strong>下列设施不符合作为安全出口条件的是（）</strong> （分值1.0）<br/>
      <ul><li>A、直通屋外者<br />
B、经走道、楼梯间或门厅能通向屋外者<br />
C、安全出口朝向封闭的院子<br />
D、通过相邻建筑或房间可通屋外者</li></ul>              你未作答
            标准答案：
                  C
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      36、<span style="color:#990000">[单选题]</span> <strong>实验室进行装修时，以下哪种做法是不正确的（）</strong> （分值1.0）<br/>
      <ul><li>A、注意用电安全，电气线路进行穿管保护<br />
B、装修使用的油漆、涂料要远离火源，室内保持良好通风<br />
C、按照自己需求设计需求私自改动电气线路<br />
D、及时打扫施工现场，清除木屑、漆垢、残渣等可燃物品</li></ul>              你未作答
            标准答案：
                  C
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      37、<span style="color:#990000">[单选题]</span> <strong>使用灭火器灭火时，要对准火焰的（）喷射</strong> （分值1.0）<br/>
      <ul><li>A、上部<br />
B、中部<br />
C、根部<br />
D、四周</li></ul>              你未作答
            标准答案：
                  C
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      38、<span style="color:#990000">[单选题]</span> <strong>家中使用电暖器等大功率电器时，以下哪种做法是正确的（）</strong> （分值1.0）<br/>
      <ul><li>A、靠近床铺，这样可以保证有效取暖<br />
B、远离床铺、窗帘、沙发等可燃物<br />
C、把衣物直接放在电暖器上烘烤<br />
D、为保持室内温度，出门时开着电暖器</li></ul>              你未作答
            标准答案：
                  B
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      39、<span style="color:#990000">[单选题]</span> <strong>报警人或知情人应协助消防人员开展以下哪些工作（）</strong> （分值1.0）<br/>
      <ul><li>A、引导消防车辆、人员到达火灾现场<br />
B、介绍起火位置（建筑）的有关情况和有无人员被困<br />
C、介绍周边可利用的消防水源<br />
D、以上均是</li></ul>              你未作答
            标准答案：
                  D
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      40、<span style="color:#990000">[单选题]</span> <strong>91、学生宿舍管理部门应当履行下列哪些安全管理职责（D）</strong> （分值1.0）<br/>
      <ul><li>A、建立由学生参加的志愿消防组织，定期进行消防演练<br />
B、加强学生宿舍用火、用电安全教育与检查<br />
C、加强夜间防火巡查，发现火灾立即组织扑救和疏散学生<br />
D、以上均是</li></ul>              你未作答
            标准答案：
                  D
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      41、<span style="color:#990000">[单选题]</span> <strong>学校各单位应当保障疏散通道、安全出口畅通，严禁以下哪种行为（）</strong> （分值1.0）<br/>
      <ul><li>A、疏散通道摆放实验仪器<br />
B、疏散通道停放电动自行车<br />
C、安全出口上锁<br />
D、以上均是</li></ul>              你未作答
            标准答案：
                  D
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      42、<span style="color:#990000">[单选题]</span> <strong>下列哪种灭火剂不可用来扑灭带电设备的火灾（）</strong> （分值1.0）<br/>
      <ul><li>A、ABC干粉灭火器<br />
B、二氧化碳灭火剂<br />
C、BC干粉灭火器<br />
D、水基灭火器</li></ul>              你未作答
            标准答案：
                  D
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      43、<span style="color:#990000">[单选题]</span> <strong>关于学生宿舍，以下哪种说法是错误（）</strong> （分值1.0）<br/>
      <ul><li>A、地下室不可当作学生宿舍 <br />
B、半地下室不可当作学生宿舍<br />
C、学生宿舍内禁止违规使用大功率电器 <br />
D、学生宿舍一楼阳台、门窗需设置防盗窗</li></ul>              你未作答
            标准答案：
                  D
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      44、<span style="color:#990000">[单选题]</span> <strong>以下哪种建筑可用作学生宿舍？（）</strong> （分值1.0）<br/>
      <ul><li>A、地下室<br />
B、半地下室<br />
C、经营易燃易爆危险用品场所<br />
D、以上均不行</li></ul>              你未作答
            标准答案：
                  D
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      45、<span style="color:#990000">[单选题]</span> <strong>消防安全四个能力不包括以下（）</strong> （分值1.0）<br/>
      <ul><li>A、提高社会单位组织人员疏散逃生的能力<br />
B、提高社会单位检查消除火灾隐患的能力<br />
C、提高社会单位组织扑救初期火灾的能力<br />
D、提高社会单位协助救援其它单位的能力</li></ul>              你未作答
            标准答案：
                  D
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      46、<span style="color:#990000">[单选题]</span> <strong>化学品的安全标签警示词不包括（）</strong> （分值1.0）<br/>
      <ul><li>A、小心<br />
B、危险<br />
C、警告<br />
D、注意</li></ul>              你未作答
            标准答案：
                  A
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      47、<span style="color:#990000">[单选题]</span> <strong>学生宿舍突然停电时，下列做法正确的是（）</strong> （分值1.0）<br/>
      <ul><li>A、将正在使用的吹风机随手放置<br />
B、切断处于使用状态的电器电源 <br />
C、将蜡烛放置在床头继续看书<br />
D、用酒精灯代替照明使用</li></ul>              你未作答
            标准答案：
                  B
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      48、<span style="color:#990000">[单选题]</span> <strong>举办集会、焰火晚会、灯会等具有火灾危险的大型活动，（）应当在具备消防安全条件后，向公安消防机构申报对活动现场进行消防安全检查</strong> （分值1.0）<br/>
      <ul><li>A、主办单位<br />
B、承办单位<br />
C、协办单位<br />
D、提供场地单位</li></ul>              你未作答
            标准答案：
                  A
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      49、<span style="color:#990000">[单选题]</span> <strong>火灾中产生的主要有毒气体有( )</strong> （分值1.0）<br/>
      <ul><li>A、CO<br />
B、NO<br />
C、N2<br />
D、NH3</li></ul>              你未作答
            标准答案：
                  A
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      50、<span style="color:#990000">[单选题]</span> <strong>单位下班前的防火巡查主要不包括（）</strong> （分值1.0）<br/>
      <ul><li>A、及时切断电源<br />
B、对一切可能遗留的火源进行清理检查<br />
C、所有人员在岗情况<br />
D、确认无遗留火种后，方可离开</li></ul>              你未作答
            标准答案：
                  C
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      51、<span style="color:#990000">[单选题]</span> <strong>学生宿舍用电时要注意消防安全，下面说法错误的是（）</strong> （分值1.0）<br/>
      <ul><li>A、不乱拉乱接电线，不超负荷用电<br />
B、使用符合国家现行标准的插线板<br />
C、外出时要切断电器电源开关<br />
D、电动自行车电瓶可以拿到宿舍内充电</li></ul>              你未作答
            标准答案：
                  D
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      52、<span style="color:#990000">[单选题]</span> <strong>某次火灾事故未造成人员伤亡，但造成的直接财产损失达110万元，该火灾危险等级为（）</strong> （分值1.0）<br/>
      <ul><li>A、特大火灾<br />
B、重大火灾<br />
C、一般火灾<br />
D、普通火灾</li></ul>              你未作答
            标准答案：
                  A
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      53、<span style="color:#990000">[单选题]</span> <strong>能与可燃物发生氧化反应的物质称为氧化剂，以下物质能作为氧化剂的是（）</strong> （分值1.0）<br/>
      <ul><li>A、氧气<br />
B、能提供氧气的含氧化合物<br />
C、氯气<br />
D、以上均可</li></ul>              你未作答
            标准答案：
                  D
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      54、<span style="color:#990000">[单选题]</span> <strong>（）都有维护消防安全、保护消防设施、预防火灾、报告火警的义务</strong> （分值1.0）<br/>
      <ul><li>A、任何单位和个人<br />
B、单位保安<br />
C、消防官兵<br />
D、公安民警</li></ul>              你未作答
            标准答案：
                  A
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      55、<span style="color:#990000">[单选题]</span> <strong>下列哪一项不属于《高等学校消防安全管理规定》要求（）</strong> （分值1.0）<br/>
      <ul><li>A、消防安全知识要纳入教学和培训内容<br />
B、每届大学生都要接受不低于4学时的消防安全教育和培训<br />
C、对于进入实验室的学生还要进行必要的安全技能和操作规程培训<br />
D、消防安全教育可作为选修课，由学校根据自身实际自行安排</li></ul>              你未作答
            标准答案：
                  D
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      56、<span style="color:#990000">[单选题]</span> <strong>《高等学校消防安全管理规定》是由国家哪个部门签署的（）</strong> （分值1.0）<br/>
      <ul><li>A、公安部<br />
B、卫生部<br />
C、教育部<br />
D、教育部联合公安部</li></ul>              你未作答
            标准答案：
                  D
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      57、<span style="color:#990000">[单选题]</span> <strong>关于干粉灭火器的使用，下列正确的是（）</strong> （分值1.0）<br/>
      <ul><li>A、在室外使用，应占据下风方向<br />
B、使用前拔下保险销<br />
C、灭救液体火灾时，应从火焰正面，对准火焰中上部喷射<br />
D、一般用于化学试剂、精密仪器的灭火</li></ul>              你未作答
            标准答案：
                  B
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      58、<span style="color:#990000">[单选题]</span> <strong>用灭火器在室外进行灭火时应占据（）灭火</strong> （分值1.0）<br/>
      <ul><li>A、上风方向<br />
B、下风方向<br />
C、着火物的上方<br />
D、着火物的下方</li></ul>              你未作答
            标准答案：
                  A
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      59、<span style="color:#990000">[单选题]</span> <strong>消防安全重点单位对每名员工应当至少（）进行一次消防安全培训</strong> （分值1.0）<br/>
      <ul><li>A、每两个月<br />
B、每半年<br />
C、每年<br />
D、每季度</li></ul>              你未作答
            标准答案：
                  B
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      60、<span style="color:#990000">[单选题]</span> <strong>建筑工程施工现场的消防安全由（）负责</strong> （分值1.0）<br/>
      <ul><li>A、建筑单位<br />
B、施工单位<br />
C、设计单位<br />
D、报建单位</li></ul>              你未作答
            标准答案：
                  B
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      61、<span style="color:#990000">[单选题]</span> <strong>储存可燃物资仓库的管理，必须执行国家有关（ ）</strong> （分值1.0）<br/>
      <ul><li>A、消防安全<br />
B、物资安全<br />
C、劳动安全</li></ul>              你未作答
            标准答案：
                  A
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      62、<span style="color:#990000">[单选题]</span> <strong>干粉灭火器适用于：</strong> （分值1.0）<br/>
      <ul><li>A、电器起火<br />
B、可燃气体起火<br />
C、有机溶剂起火<br />
D、以上都是</li></ul>              你未作答
            标准答案：
                  D
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      63、<span style="color:#990000">[单选题]</span> <strong>公安消防队救火（）</strong> （分值1.0）<br/>
      <ul><li>A、只收救火成本费<br />
B、收取所有费用<br />
C、不收任何费用</li></ul>              你未作答
            标准答案：
                  C
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      64、<span style="color:#990000">[单选题]</span> <strong>违反《中华人民共和国消防法》行为，构成犯罪的，应：</strong> （分值1.0）<br/>
      <ul><li>A、依法给予行政处罚<br />
B、依法追究刑事责任<br />
C、给予罚款或拘留</li></ul>              你未作答
            标准答案：
                  B
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      65、<span style="color:#990000">[单选题]</span> <strong>阻拦报火警或者谎报火警的给予（ ）处罚。</strong> （分值1.0）<br/>
      <ul><li>A、劳动教养<br />
B、撤掉其电话<br />
C、警告、罚款或者十日以下拘留</li></ul>              你未作答
            标准答案：
                  C
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      66、<span style="color:#990000">[单选题]</span> <strong>有机物或能与水发生剧烈化学反应的药品着火，应用 （ ），以免扑救不当造成更大损害。</strong> （分值1.0）<br/>
      <ul><li>A、其他有机物灭火<br />
B、自来水灭火<br />
C、灭火器或沙子扑灭</li></ul>              你未作答
            标准答案：
                  C
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      67、<span style="color:#990000">[单选题]</span> <strong>从下列选项中选择万一发生电气火灾后首先应该采取的第一条措施</strong> （分值1.0）<br/>
      <ul><li>A、打电话报警<br />
B、切断电源<br />
C、扑灭明火<br />
D、保护现场，分析火因，以便采取措施，杜绝隐患</li></ul>              你未作答
            标准答案：
                  B
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      68、<span style="color:#990000">[单选题]</span> <strong>我国大陆通用的火警电话号码是：</strong> （分值1.0）<br/>
      <ul><li>A、991<br />
B、119<br />
C、911</li></ul>              你未作答
            标准答案：
                  B
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      69、<span style="color:#990000">[单选题]</span> <strong>由于行为人的过失引起火灾，造成严重后果的行为，构成（ ）</strong> （分值1.0）<br/>
      <ul><li>A、纵火罪<br />
B、失火罪<br />
C、重大责任事故罪</li></ul>              你未作答
            标准答案：
                  B
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      70、<span style="color:#990000">[单选题]</span> <strong>灭火器上的压力表用红、黄、绿三色表示灭火器的压力情况，当指针指在绿色区域表示：</strong> （分值1.0）<br/>
      <ul><li>A、正常<br />
B、偏高<br />
C、偏低</li></ul>              你未作答
            标准答案：
                  A
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      71、<span style="color:#990000">[单选题]</span> <strong>发生火灾时，正确的安全疏散主要有三个方向，向下可以跑到地面，向上可以爬到屋顶，还可以（）</strong> （分值1.0）<br/>
      <ul><li>A、躲到角落里<br />
B、向外逃到阳台<br />
C、钻到阁楼、大橱等处避难</li></ul>              你未作答
            标准答案：
                  B
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      72、<span style="color:#990000">[单选题]</span> <strong>当遇到火灾时，要迅速向（ ）逃生。</strong> （分值1.0）<br/>
      <ul><li>A、着火相反的方向<br />
B、人员多的方向<br />
C、安全出口的方向</li></ul>              你未作答
            标准答案：
                  C
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      73、<span style="color:#990000">[单选题]</span> <strong>泡沫灭火器不能用于扑救 （ ）火灾。</strong> （分值1.0）<br/>
      <ul><li>A、塑料<br />
B、汽油<br />
C、金属钠</li></ul>              你未作答
            标准答案：
                  C
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      74、<span style="color:#990000">[单选题]</span> <strong>公共场所安全出口的疏散门应（ ）。</strong> （分值1.0）<br/>
      <ul><li>A、双向开启<br />
B、向外开启<br />
C、向内开启 </li></ul>              你未作答
            标准答案：
                  B
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      75、<span style="color:#990000">[单选题]</span> <strong>使用灭火器扑救火灾时要对准火焰的什么部位喷射。</strong> （分值1.0）<br/>
      <ul><li>A、上部<br />
B、中部<br />
C、根部<br />
D、中上部</li></ul>              你未作答
            标准答案：
                  C
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      76、<span style="color:#990000">[单选题]</span> <strong>公安消防人员在灭火过程中，应当（ ）。</strong> （分值1.0）<br/>
      <ul><li>A、优先救人<br />
B、优先抢救财物<br />
C、优先灭火 </li></ul>              你未作答
            标准答案：
                  A
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      77、<span style="color:#990000">[单选题]</span> <strong>按照国家工程建筑消防技术标准施工的项目竣工时，（ ）经公安消防机构进行消防验收。</strong> （分值1.0）<br/>
      <ul><li>A、必须<br />
B、可以<br />
C、应当</li></ul>              你未作答
            标准答案：
                  A
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      78、<span style="color:#990000">[单选题]</span> <strong>火灾中对人员威胁最大的是（ ）。</strong> （分值1.0）<br/>
      <ul><li>A、火<br />
B、烟气<br />
C、可燃物</li></ul>              你未作答
            标准答案：
                  B
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      79、<span style="color:#990000">[单选题]</span> <strong>身上着火后,下列哪种灭火方法是错误的？</strong> （分值1.0）<br/>
      <ul><li>A、就地打滚<br />
B、用厚重衣物覆盖压灭火苗<br />
C、迎风快跑<br />
D、大量水冲或跳入水中</li></ul>              你未作答
            标准答案：
                  C
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      80、<span style="color:#990000">[单选题]</span> <strong>《中华人民共和国消防法》自（ ）起施行。</strong> （分值1.0）<br/>
      <ul><li>A、1997年<br />
B、1998年<br />
C、2000年</li></ul>              你未作答
            标准答案：
                  B
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      81、<span style="color:#990000">[单选题]</span> <strong>疏散指示灯，一般设在距离地面不超过（）的墙面上</strong> （分值1.0）<br/>
      <ul><li>A、0.5米<br />
B、0.8米<br />
C、1米<br />
D、1.5米</li></ul>              你未作答
            标准答案：
                  C
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      82、<span style="color:#990000">[单选题]</span> <strong>火灾可分为A、B、C、D四类，A、B、C、D分别指的是什么？（）</strong> （分值1.0）<br/>
      <ul><li>A、可燃固体、可燃气体、可燃液体、可燃金属<br />
B、可燃固体、可燃液体、可燃气体、可燃金属<br />
C、可燃液体、可燃气体、可燃金属、可燃固体<br />
D、可燃金属、可燃固体、可燃液体、可燃气体</li></ul>              你未作答
            标准答案：
                  B
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      83、<span style="color:#990000">[单选题]</span> <strong>电气设备起火时，应选用以下（）灭火器灭火</strong> （分值1.0）<br/>
      <ul><li>A、水<br />
B、ABC干粉灭火器<br />
C、泡沫灭火器<br />
D、以上都可以</li></ul>              你未作答
            标准答案：
                  B
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      84、<span style="color:#990000">[单选题]</span> <strong>单位应当落实逐级消防安全责任制和岗位消防安全责任制，明确逐级和岗位消防安全职责，确定各级、各岗位的（），并以文件形式公布</strong> （分值1.0）<br/>
      <ul><li>A、消防安全责任人<br />
B、消防管理人<br />
C、消防安全管理人<br />
D、企业负责人</li></ul>              你未作答
            标准答案：
                  A
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      85、<span style="color:#990000">[单选题]</span> <strong>灭火器压力表用红、黄、绿三色表示压力情况，当指针指在绿色区域表示（）</strong> （分值1.0）<br/>
      <ul><li>A、正常<br />
B、偏低<br />
C、偏高<br />
D、其他</li></ul>              你未作答
            标准答案：
                  A
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      86、<span style="color:#990000">[单选题]</span> <strong>家用电器发生火灾，在没有灭火器的情况下应先（）</strong> （分值1.0）<br/>
      <ul><li>A、用水扑救<br />
B、用毛毯包裹<br />
C、切断电源<br />
D、用湿毛巾覆盖</li></ul>              你未作答
            标准答案：
                  C
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      87、<span style="color:#990000">[单选题]</span> <strong>火场中防止烟气危害最简单的方法是( )</strong> （分值1.0）<br/>
      <ul><li>A、跳楼或窗口逃生<br />
B、大声呼救<br />
C、用湿毛巾或衣服捂住口鼻低姿势沿疏散通道逃生<br />
D、尽量憋气</li></ul>              你未作答
            标准答案：
                  C
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      88、<span style="color:#990000">[单选题]</span> <strong>据统计，火灾中死亡的人有80%以上属于（）</strong> （分值1.0）<br/>
      <ul><li>A、被火烧死<br />
B、烟气窒息致死<br />
C、跳楼致死<br />
D、惊吓致死</li></ul>              你未作答
            标准答案：
                  B
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      89、<span style="color:#990000">[单选题]</span> <strong>根据刑法规定，失火罪处以（）年有期徒刑</strong> （分值1.0）<br/>
      <ul><li>A、1-2年<br />
B、2-3年<br />
C、3-6年<br />
D、3-7年</li></ul>              你未作答
            标准答案：
                  D
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      90、<span style="color:#990000">[单选题]</span> <strong>当打开房门闻到燃气气味时，要迅速( )，以防止引起火灾。</strong> （分值1.0）<br/>
      <ul><li>A、打开燃气灶具查找漏气部位<br />
B、打开门窗通风<br />
C、立刻打电话给燃气公司</li></ul>              你未作答
            标准答案：
                  B
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      91、<span style="color:#990000">[单选题]</span> <strong>防火门应该是朝疏散方向开启的（）</strong> （分值1.0）<br/>
      <ul><li>A、弹簧门<br />
B、平开门<br />
C、推拉门<br />
D、转门</li></ul>              你未作答
            标准答案：
                  C
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      92、<span style="color:#990000">[单选题]</span> <strong>带电的电气设备以及发电机、电动机等应使用（）灭火</strong> （分值1.0）<br/>
      <ul><li>A、水<br />
B、泡沫灭火器<br />
C、ABC干粉灭火器、二氧化碳灭火器<br />
D、干砂</li></ul>              你未作答
            标准答案：
                  C
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      93、<span style="color:#990000">[单选题]</span> <strong>当打开房门闻到煤气气味，首先应该怎么办？（）</strong> （分值1.0）<br/>
      <ul><li>A．打开煤气灶具查找漏气部位<br />
B、打开灯查找漏气部位<br />
C、打开窗门通风<br />
D、打开通气扇通风</li></ul>              你未作答
            标准答案：
                  C
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      94、<span style="color:#990000">[单选题]</span> <strong>火灾初起阶段是扑救火灾( )的阶段。</strong> （分值1.0）<br/>
      <ul><li>A、最不利<br />
B、最有利<br />
C、较不利</li></ul>              你未作答
            标准答案：
                  B
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      95、<span style="color:#990000">[单选题]</span> <strong>火灾蔓延的途径是:</strong> （分值1.0）<br/>
      <ul><li>A、热传导<br />
B、热对流<br />
C、热辐射<br />
D、以上都是</li></ul>              你未作答
            标准答案：
                  D
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      96、<span style="color:#990000">[单选题]</span> <strong>被火困在室内,如何逃生？</strong> （分值1.0）<br/>
      <ul><li>A、跳楼<br />
B、到窗口或阳台挥动物品求救、用床单或绳子拴在室内牢固处下到 下一层逃生<br />
C、躲到床下,等待救援<br />
D、打开门,冲出去</li></ul>              你未作答
            标准答案：
                  B
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      97、<span style="color:#990000">[单选题]</span> <strong>我国消防宣传活动日是每年的</strong> （分值1.0）<br/>
      <ul><li>A、11月9日<br />
B、1月19日<br />
C、9月11日<br />
D、9月10日</li></ul>              你未作答
            标准答案：
                  A
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      98、<span style="color:#990000">[单选题]</span> <strong>我国消防工作的方针是：</strong> （分值1.0）<br/>
      <ul><li>A、群防群治<br />
B、遏制种特大火灾<br />
C、预防为主，防消结合</li></ul>              你未作答
            标准答案：
                  C
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      99、<span style="color:#990000">[单选题]</span> <strong>可以用水扑灭的火灾是下列哪种物质？</strong> （分值1.0）<br/>
      <ul><li>A、油类起火<br />
B、酒精起火<br />
C、电器起火<br />
D、棉被起火</li></ul>              你未作答
            标准答案：
                  D
              
              </div>
            <div class="shiti" style='border-bottom:1px dotted #ccc;margin: 15px'>
      <img style="float:right" src="/template/images/wrong.gif"/>      100、<span style="color:#990000">[单选题]</span> <strong>在火灾初发阶段，应采取哪种方法撤离？</strong> （分值1.0）<br/>
      <ul><li>A、乘坐电梯<br />
B、用湿毛巾捂住口鼻低姿从安全通道撤离<br />
C、跳楼逃生<br />
D、跑到楼顶呼救</li></ul>              你未作答
            标准答案：
                  B
              
              </div>

'''
# 去掉所有的空白符，包括换行符和空格、制表符
answer_source = re.sub('\s', '', answer_source)
obj1 = re.compile(r'<form method="post" id="dati">(?P<allquiz>.*?)<div class="nav">',re.S)
obj2 = re.compile(r'<h3>(?P<quiz>.*?)</h3>',re.S)
safari = Chrome()
url = 'https://labsafe.hnu.edu.cn/labexam/index.php'
safari.get(url)
time.sleep(1)
el = safari.find_element(By.XPATH,'//*[@id="formExam"]/div/a/input')
el.click()
username = '202311020126'
password = 'Hnu_hzy0507'
safari.find_element(By.XPATH,'//*[@id="username"]').send_keys(username)
time.sleep(1)
safari.find_element(By.XPATH,'//*[@id="password"]').send_keys(password)
time.sleep(1)
safari.find_element(By.XPATH,'//*[@id="dl"]').click()
time.sleep(3)
safari.find_element(By.XPATH,'//*[@id="article"]/div[3]/div[2]/ul/a[1]/li').click()
time.sleep(1)
safari.find_element(By.XPATH,'//*[@id="tkqcl"]/ul/li/label').click()
time.sleep(1)
safari.find_element(By.XPATH,'//*[@id="article"]/div[4]/div[2]/div/a[1]').click()
time.sleep(1)
def clickanswer(l:list,page,index):
    if l == None or l[0] == None:
        print('no answer')
    elif l[0] == '正确' or l[0] == 'A':
        _id = 'ti_'+ str(page*10+index) + '_0'
        safari.find_element(By.ID,_id).click()
    elif l[0] == '错误' or l[0] == 'B':
        _id = 'ti_'+ str(page*10+index) + '_1'
        safari.find_element(By.ID,_id).click()
    elif l[0] == 'C':
        _id = 'ti_'+ str(page*10+index) + '_2'
        safari.find_element(By.ID,_id).click()
    elif l[0] == 'D':
        _id = 'ti_'+ str(page*10+index) + '_3'
        safari.find_element(By.ID,_id).click()
    pass
def findanswer(s:str,answersource):
    s = s.split('、')[1]
    s = s.replace('?', '\\?')
    s = s.replace('(', '\\(')
    s = s.replace(')', '\\)')
    s = s + '.*?你未作答标准答案：(?P<answer>.*?)</div>'
    pattern = re.compile(s)
    answer = re.findall(pattern, answersource)
    return answer
for page in range(10): #i是页码
    if page == 0:
        page_source = safari.page_source
        allquiz = obj1.findall(page_source)
        quizlist = []
        answerlist = []
        quizlist.append(obj2.findall(allquiz[0]))
        for qu in quizlist[0]:
            answer = findanswer(qu,answer_source)
            answerlist.append(answer)
        # <input type="radio" name="ti_91" id="ti_91_1" value="B">
        print(answerlist)
        safari.find_element(By.XPATH,'//*[@id="dati"]/div[11]/input[1]').click()
        time.sleep(1)
    elif 1<=page<9:
        page_source = safari.page_source
        allquiz = obj1.findall(page_source)
        quizlist = []
        answerlist = []
        quizlist.append(obj2.findall(allquiz[0]))
        for qu in quizlist[0]:
            answer = findanswer(qu,answer_source)
            answerlist.append(answer)
        print(answerlist)
        safari.find_element(By.XPATH, '//*[@id="dati"]/div[11]/input[2]').click()
        time.sleep(1)
    else:
        page_source = safari.page_source
        allquiz = obj1.findall(page_source)
        quizlist = []
        answerlist = []
        quizlist.append(obj2.findall(allquiz[0]))
        for qu in quizlist[0]:
            answer = findanswer(qu,answer_source)
            answerlist.append(answer)
        print(answerlist)