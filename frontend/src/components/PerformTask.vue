<template>
  <div>
    <el-header class="header-style">
      <el-row>
        <el-col :span="8">
          <el-breadcrumb separator="/" class="header-breadcrumb">
            <el-breadcrumb-item :to="{ path: '/' }">奶黄包</el-breadcrumb-item>
            <el-breadcrumb-item>任务选择</el-breadcrumb-item>
            <el-breadcrumb-item>{{ materialType }}</el-breadcrumb-item>
            <el-breadcrumb-item v-if="isTest"
              ><span style="color:#5EABBF;font-size=30px;font-weight: bold;"
                >资质测试</span
              ></el-breadcrumb-item
            >
            <el-breadcrumb-item
              >题目：{{ currentIndex + 1 }}</el-breadcrumb-item
            >
          </el-breadcrumb>
          <span style="float: left; font-size: 25px; font-weight: bold">
            {{ taskName }}
          </span>
        </el-col>
        <el-col :span="16">
          <el-row style="height:100%;display:flex;align-items: center;">
            <el-col :span="5" style="background-color:aquamarine">
              <CustomButton
                @click="finalSubmit"
                isRound="true"
                v-if="false"
                normalColor="#FBE484"
                height="40px"
                width="150px"
                title="提交任务"
                style="display:flex;justify-content:center;align-items:center;"
              />
            </el-col>
            <el-col :span="6">
              <CustomButton
                @click="jumpDialogVisible = true"
                isRound="true"
                height="40px"
                width="150px"
                title="题目跳转"
                style="display:flex;justify-content:center;align-items:center;"
              />
            </el-col>
            <el-col :span="6">
              <CustomButton
                @click="submitAnswers"
                isRound="true"
                height="40px"
                width="150px"
                title="提交本题"
                style="display:flex;justify-content:center;align-items:center;"
              />
            </el-col>
            <el-col :span="6">
              <CustomButton
                @click="quitPerform"
                isRound="true"
                height="40px"
                width="150px"
                title="退出答题"
                style="display:flex;justify-content:center;align-items:center;"
              />
            </el-col>
          </el-row>
        </el-col>
      </el-row>
    </el-header>
    <el-row :gutter="20" style="margin-top: 20px">
      <el-col :span="15">
        <el-main class="main-style-two" style="height: calc(100vh - 220px)">
          <el-row
            class="main-style"
            v-for="material in materialList"
            :key="material"
          >
            <!-- {{material['fileNotes']}} -->
            <PerformTaskMaterial ref="materialBlock" :materialInfo="material">
            </PerformTaskMaterial>
          </el-row>
        </el-main>
      </el-col>
      <el-col :span="9">
        <el-main class="main-style-two" style="height: calc(100vh - 220px)">
          <el-row
            class="question-row"
            v-for="question in questionList"
            :key="question"
          >
            <span class="header-title" style="margin: auto, auto, auto, 20px">
              {{
                question["index"] +
                ".[" +
                question["questionTypeName"] +
                "]: " +
                question["questionDescription"]
              }}
            </span>
            <CustomButton
              @click="
                currentQuestionIndex = question['index'] - 1;
                clickFillBlank(
                  question['targetIndex'] - 1,
                  question['minOptionNum'],
                  question['maxOptionNum'],
                  question['index'] - 1
                );
              "
              v-if="question['questionType'] == 3"
              isRound="true"
              style="float: right; right: 0px; top: 5px; position: absolute"
              height="30px"
              width="100px"
              title="点击框图"
            />
            <el-table
              v-if="
                question['questionType'] == 0 || question['questionType'] == 1
              "
              :data="question['optionList']"
              :style="table"
              ref="regTable"
              :key="tableKey"
              @selection-change="
                handleSelectionChange(
                  $event,
                  question['minOptionNum'],
                  question['maxOptionNum'],
                  question['index'] - 1
                )
              "
              class="selection-table"
            >
              <el-table-column type="selection" width="50"> </el-table-column>
              <el-table-column prop="name" label="选项" width="100">
              </el-table-column>
              <el-table-column prop="content" label="选项内容" width="200">
                <template v-slot="scope">
                  <div>{{ scope.row.content }}</div>
                </template>
              </el-table-column>

              <el-table-column prop="" label="" width=""> </el-table-column>

              <el-table-column prop="" label="删除" width="">
                <span class="iconfont icon-menu"></span>
              </el-table-column>
            </el-table>
            <el-input
              v-if="question['questionType'] == 2"
              v-model="this.ansList[question['index'] - 1]"
              :rows="3"
              type="textarea"
              placeholder="请输入填空题答案"
              resize="none"
              :maxlength="question['maxOptionNum']"
              show-word-limit
              style="margin: 20px"
            />
          </el-row>
        </el-main>
      </el-col>
    </el-row>
    <el-dialog v-model="fillBlankDialogVisible" title="请进行框图">
      <el-container v-if="imageLoading">
        <div
          style="
            position: relative;
            width: 250px;
            height: 200px;
            margin-left: auto;
            margin-right: auto;
          "
        >
          <div
            style="
              position: absolute;
              bottom: 50px;
              left: 60px;
              width: 250px;
              height: 250px;
            "
          >
            <div
              style="
                flex-direction: column;
                position: absolute;
                bottom: 0px;
                margin-left: auto;
                margin-right: auto;
                text-align: center;
              "
            >
              <el-image
                style="width: 88px; height: 80px"
                fit="cover"
                :src="require('@/assets/images/logo_small.png')"
                class="jump-logo"
              ></el-image>
              <div class="jump-shadow"></div>
            </div>
          </div>
          <div
            style="
              position: absolute;
              bottom: -210px;
              left: -20px;
              width: 250px;
              height: 250px;
            "
          >
            <span
              style="color: #5eabbf; font-size: 20px; font-family: YouSheBlack"
            >
              正在加载图片，请稍等~
            </span>
          </div>
        </div>
      </el-container>
      <ImageFramer
        v-else
        ref="MyImageFramer"
        style="width: 100%"
        :minFrameNum="currentMin"
        :maxFrameNum="currentMax"
        :src="currentImageSrc"
        :initRects="initRects"
      />
      <span class="dialog-footer">
        <el-row style="height: 50px">
          <el-col :span="20"> </el-col>
          <el-col :span="4">
            <CustomButton
              @click="getFillBlankAns"
              style="margin-left: 20px"
              isRound="true"
              title="确定"
            />
          </el-col>
        </el-row>
      </span>
    </el-dialog>

    <el-dialog
      v-model="jumpDialogVisible"
      title="设置跳转位置"
      width="22%"
      style="display: flex; flex-wrap: wrap"
    >
      <el-button
        style="width: 40px; height: 40px; margin: 5px"
        :type="getListButtonType(state['state'], state['index'])"
        plain
        v-for="state in stateList"
        :key="state"
        @click="jumpQuestion(state['index'])"
        >{{ state["index"] }}</el-button
      >
      <span class="dialog-footer">
        <el-row style="height: 50px; margin-top: 20px">
          <CustomButton
            @click="jumpDialogVisible = false"
            style="margin-left: 20px"
            isRound="true"
            title="取消跳转"
          />
        </el-row>
      </span>
    </el-dialog>

    <el-dialog
      v-model="testResultDialogVisible"
      @close="closeTestResultDialog"
      width="40%"
      style="display: flex; flex-wrap: wrap"
    >
      <el-main v-if="!passTest">
        <el-row style="margin-bottom: 20px">
          <span style="font-weight: bold; font-size: 20px">
            很抱歉，您未能通过资质测试
          </span>
        </el-row>
        <el-row>
          <span> 您的正答率： </span>
          <span style="font-weight: bold; font-size: 15px; color: #5eabbf">
            {{ percentage }}
          </span>
        </el-row>
        <span class="dialog-footer">
          <el-row style="height: 50px; margin-top: 20px">
            <CustomButton
              @click="
                testResultDialogVisible = false;
                closeTestResultDialog();
              "
              style="margin-left: 20px"
              isRound="true"
              title="退出答题"
            />
          </el-row>
        </span>
      </el-main>
      <el-main v-else>
        <el-row style="margin-bottom: 20px">
          <span style="font-weight: bold; font-size: 20px">
            恭喜您通过资质测试！请继续答题
          </span>
        </el-row>
        <el-row>
          <span> 您的正答率： </span>
          <span style="font-weight: bold; font-size: 15px; color: #5eabbf">
            {{ percentage }}
          </span>
        </el-row>
        <span class="dialog-footer">
          <el-row style="height: 50px; margin-top: 20px">
            <CustomButton
              @click="
                testResultDialogVisible = false;
                closeTestResultDialog();
              "
              style="margin-left: 20px"
              isRound="true"
              title="正式答题"
            />
          </el-row>
        </span>
      </el-main>
    </el-dialog>

    <el-dialog
      v-model="finalSubmitDialogVisible"
      width="40%"
      style="display: flex; flex-wrap: wrap"
    >
      <el-main>
        <el-row style="margin-bottom: 20px">
          <span style="font-weight: bold; font-size: 20px">
            您已完成所有题目，请问您现在是否要提交该任务？
          </span>
        </el-row>
        <span class="dialog-footer">
          <el-row style="height: 50px; margin-top: 20px">
            <CustomButton
              @click="
                finalSubmitDialogVisible = false;
                finalSubmit();
              "
              style="margin: auto"
              isRound="true"
              title="提交任务"
            />
            <CustomButton
              @click="finalSubmitDialogVisible = false"
              style="margin: auto"
              isRound="true"
              title="暂不提交"
            />
          </el-row>
        </span>
      </el-main>
    </el-dialog>

    <el-dialog
      v-model="submitOutcomeDialogVisible"
      @close="closeSubmitOutcomeDialog"
      width="40%"
      style="display: flex; flex-wrap: wrap"
    >
      <el-main v-if="!passInsertionTest">
        <el-row style="margin-bottom: 20px">
          <span style="font-weight: bold; font-size: 40px"> 任务结算 </span>
        </el-row>
        <el-row style="margin-bottom: 20px">
          <span style="font-weight: bold; font-size: 20px">
            很抱歉，由于您本次答题状态不佳，
          </span>
        </el-row>
        <el-row>
          <span> 今天已经违规： </span>
          <span style="font-weight: bold; font-size: 15px; color: red">
            {{ todayViolationNum }}
          </span>
          <span> 次，最多可以违规： </span>
          <span style="font-weight: bold; font-size: 15px; color: red">
            {{ perDayViolationNum }}
          </span>
          <span> 次。 </span>
        </el-row>
        <el-row v-if="isPunish">
          <span style="font-weight: bold; font-size: 15px; color: red">
            您由于今日违规次数过多，将损失部分经验！
          </span>
        </el-row>
        <span class="dialog-footer">
          <el-row style="height: 50px; margin-top: 20px">
            <CustomButton
              @click="
                submitOutcomeDialogVisible = false;
                closeSubmitOutcomeDialog();
              "
              style="margin-left: 20px"
              isRound="true"
              title="退出任务"
            />
          </el-row>
        </span>
      </el-main>
      <el-main v-else>
        <el-row style="margin-bottom: 20px">
          <span style="font-weight: bold; font-size: 40px"> 任务结算 </span>
        </el-row>
        <el-row style="margin-bottom: 20px">
          <span style="font-weight: bold; color: #5eabbf; font-size: 20px">
            恭喜您顺利完成本次任务！
          </span>
        </el-row>
        <el-row>
          <span> 您在本次任务中获得甜甜圈： </span>
          <span style="font-weight: bold; font-size: 15px; color: #5eabbf">
            {{ getDonutNum }}
          </span>
        </el-row>
        <el-row>
          <span> 您当前的甜甜圈余额为： </span>
          <span style="font-weight: bold; font-size: 15px; color: #5eabbf">
            {{ nowDonutNumber }}
          </span>
        </el-row>
        <el-row>
          <span> 您在本次任务中获得经验： </span>
          <span style="font-weight: bold; font-size: 15px; color: #5eabbf">
            {{ getExpNum }}
          </span>
        </el-row>
        <el-row v-if="isUpgrade">
          <span> 同时恭喜您的等级提升！您当前的等级为 </span>
          <span style="font-weight: bold; font-size: 15px; color: #5eabbf">
            {{ nowCreditRank }}
          </span>
        </el-row>
        <span class="dialog-footer">
          <el-row style="height: 50px; margin-top: 20px">
            <CustomButton
              @click="
                submitOutcomeDialogVisible = false;
                closeSubmitOutcomeDialog();
              "
              style="margin-left: 20px"
              isRound="true"
              title="退出任务"
            />
          </el-row>
        </span>
      </el-main>
    </el-dialog>

    <el-dialog
      v-model="taskOverDialogVisible"
      title="提示"
      width="50%"
      style="display: flex; flex-wrap: wrap"
    >
      <el-main>
        <el-row style="margin-bottom: 20px">
          <span style="font-weight: bold; font-size: 30px">
            很抱歉，该任务已经被发布者临时终止！
          </span>
        </el-row>
        <el-row style="margin-bottom: 20px">
          <span style="font-size: 20px"> 请您退出本次答题~ </span>
        </el-row>
        <span class="dialog-footer">
          <el-row style="height: 50px; margin-top: 20px">
            <CustomButton
              @click="
                taskOverDialogVisible = false;
                closeSubmitOutcomeDialog();
              "
              style="margin-left: 20px"
              isRound="true"
              title="退出任务"
            />
          </el-row>
        </span>
      </el-main>
    </el-dialog>

    <el-dialog
      v-model="testStartDialogVisible"
      title="提示"
      width="40%"
      style="display: flex; flex-wrap: wrap"
    >
      <el-main style="margin-left: -20px">
        <el-row style="margin-bottom: 10px">
          <span style="font-weight: bold; font-size: 30px; color: #5eabbf">
            感谢领取本次任务！
          </span>
        </el-row>
        <el-row style="margin-bottom: 20px">
          <span style="font-weight: bold; font-size: 25px">
            现在进行资质测试。
          </span>
        </el-row>
        <el-row style="margin-bottom: 20px">
          <span style="font-size: 20px">
            测试共{{ stateList.length }}道题目，完成测试后即可正式开始任务~
          </span>
        </el-row>
        <span class="dialog-footer">
          <el-row style="height: 50px; margin-top: 20px">
            <CustomButton
              @click="testStartDialogVisible = false"
              style="margin-left: 20px"
              isRound="true"
              title="开始测试"
            />
          </el-row>
        </span>
      </el-main>
    </el-dialog>
  </div>
</template>

<script>
import axios from "axios";
import CustomButton from "./CustomButton.vue";
import PerformTaskMaterial from "@/components/PerformTaskMaterial.vue";
import ImageFramer from "@/components/ImageFramer.vue";

export default {
  name: "PerformTask",
  inject: ["reload"],
  components: {
    CustomButton,
    PerformTaskMaterial,
    ImageFramer,
  },
  props: {
    username: String,
    login: Boolean,
    taskId: Number,
    taskName: String,
    imageSrc: String,
    materialType: String,
  },
  data() {
    return {
      imageFile: null,
      questionList: [],
      materialList: [],
      ansList: [],
      lastSelectedList: [],
      stateList: [],
      currentImageSrc: undefined,
      currentIndex: -1,
      fillBlankDialogVisible: false,
      jumpDialogVisible: false,
      currentMin: -1,
      currentMax: -1,
      currentQuestionIndex: -1,
      isTest: false,
      passTest: false,
      testStartDialogVisible: false,
      testStartDialogVisibleFirst: true,
      testResultDialogVisible: false,
      finalSubmitDialogVisible: false,
      submitOutcomeDialogVisible: false,
      taskOverDialogVisible: false,
      percentage: "114.514%",
      //提交之后的临时量
      passInsertionTest: false,
      isPunish: false,
      todayViolationNum: -1,
      perDayViolationNum: -1,
      getExpNum: -1,
      getDonutNum: -1,
      isUpgrade: false,
      nowCreditRank: -2,
      nowDonutNumber: -1,
      initRects: [],
      initAnsList: [],
      initAnsListStr: "",
      initingSelection: true,
      tableKey: 0,
      isFinished: false,
      imageLoading: false,
    };
  },
  mounted() {
    //nextTick:加载完参数后再运行下面的
    this.$nextTick(() => {
      this.getProblemInfo("init");
    });
  },
  methods: {
    finalSubmit() {
      axios
        .post("http://101.42.118.80:8000/final_submit/", {
          username: this.username,
          taskId: this.taskId,
        })
        .then((res) => {
          this.$message({
            type: "success",
            message: "提交成功!",
          });
          this.passInsertionTest = res.data["passInsertionTest"];
          this.isPunish = res.data["isPunish"];
          this.todayViolationNum = res.data["todayViolationNum"];
          this.perDayViolationNum = res.data["perDayViolationNum"];
          this.getExpNum = res.data["getExpNum"];
          this.getDonutNum = res.data["getDonutNum"];
          this.isUpgrade = res.data["isUpgrade"];
          this.nowCreditRank = res.data["nowCreditRank"];
          this.nowDonutNumber = res.data["nowDonutNumber"];
          this.submitOutcomeDialogVisible = true;
        })
        .catch((error) => {
          this.$message({
            type: "error",
            message: "提交失败!",
          });
          console.log(error);
        });
    },
    closeTestResultDialog() {
      if (!this.passTest) {
        //如果没有通过资质测试
        this.$router.push({
          //跳转到个人中心领取列表
          name: "mine",
          query: {
            username: this.username,
            imageSrc: this.imageSrc,
            defaultActive: "2",
          },
        });
      } else {
        this.isFinished = false;
        this.getProblemInfo("init");
      }
    },
    closeSubmitOutcomeDialog() {
      this.$router.push({
        //跳转到个人中心领取列表
        name: "mine",
        query: {
          username: this.username,
          imageSrc: this.imageSrc,
          defaultActive: "2",
        },
      });
    },
    getListButtonType(input, index) {
      var output = input ? "success" : "amy";
      if (index - 1 == this.currentIndex) {
        output = "primary";
      }
      return output;
    },
    getProblemInfo(type, jmpTarget = -1) {
      // dom元素更新后执行，因此这里能正确打印更改之后的值
      axios
        .get("http://101.42.118.80:8000/perform_basic_info/", {
          params: {
            username: this.username,
            taskId: this.taskId,
            type: type,
            jmpTarget: jmpTarget,
          },
        })
        .then((res) => {
          this.ansChanged = false;
          this.questionList = res.data["questionList"];
          this.materialList = res.data["materialList"];
          this.stateList = res.data["problemStateList"];
          this.isTest = res.data["isTest"];
          if (
            this.isTest &&
            type == "init" &&
            this.testStartDialogVisibleFirst
          ) {
            this.testStartDialogVisible = false;
            this.testStartDialogVisibleFirst = false;
          }
          this.currentIndex = res.data["currentIndex"] - 1; //计算机地址
          this.ansList = [];
          var tempAnswerList = res.data["answerList"];
          this.initAnsList = res.data["answerList"];
          this.initingSelection = true;
          if (this.initAnsList.length == 0) {
            for (var i = 0; i < this.questionList.length; i++) {
              this.initAnsList.push("");
            }
          }
          for (var i = 0; i < this.questionList.length; i++) {
            this.lastSelectedList.push(undefined);
            var tempQuestion = this.questionList[i];
            // 如果题目是选择题
            if (
              tempQuestion["questionType"] == 0 ||
              tempQuestion["questionType"] == 1
            ) {
              this.ansList.push([]);
              // 初始化对应串
              var k = 0;
              for (var j = 0; j < tempQuestion["optionList"].length; j++) {
                var tempName = tempQuestion["optionList"][j]["name"];
                if (
                  k < this.initAnsList[i].length &&
                  tempName == this.initAnsList[i][k]
                ) {
                  this.ansList[i].push({
                    index: tempQuestion["optionList"][j]["index"],
                    name: tempQuestion["optionList"][j]["name"],
                    selected: 1,
                  });
                  k++;
                } else {
                  this.ansList[i].push({
                    index: tempQuestion["optionList"][j]["index"],
                    name: tempQuestion["optionList"][j]["name"],
                    selected: 0,
                  });
                }
              }
              // 否则
            } else {
              this.ansList.push(tempAnswerList[i]);
            }
          }
          this.initAnsListStr = JSON.stringify(this.ansList);
          this.updateSelect();
        })
        .catch();
    },
    updateSelect() {
      //更新列表
      this.$nextTick(() => {
        for (var i = 0; i < this.questionList.length; i++) {
          if (
            this.questionList[i]["questionType"] == 0 ||
            this.questionList[i]["questionType"] == 1
          ) {
            //如果本题是选择题
            let table = this.questionList[i]["optionList"];

            table.forEach((row) => {
              if (this.ansList[i][row["index"]]["selected"] == 1) {
                this.$refs.regTable[i].toggleRowSelection(row, true);
              }
            });
          }
        }

        this.initingSelection = false;
      });
    },
    async previousQuestion() {
      if (this.initAnsListStr != JSON.stringify(this.ansList)) {
        await this.$confirm("请问是否需要提交当前答案？", "提示", {
          confirmButtonText: "确定",
          cancelButtonText: "取消",
          type: "warning",
        })
          .then(() => {
            if (!this.submitAnswers()) {
              return;
            }
          })
          .catch(() => {});
      }
      this.reload();
      this.getProblemInfo("last");
      this.reload();
    },
    async jumpQuestion(index) {
      if (this.initAnsListStr != JSON.stringify(this.ansList)) {
        await this.$confirm("请问是否需要提交当前答案？", "提示", {
          confirmButtonText: "是",
          cancelButtonText: "否",
          type: "warning",
        })
          .then(() => {
            if (!this.submitAnswers()) {
              return;
            }
          })
          .catch(() => {});
      }

      this.jumpDialogVisible = false;
      this.$nextTick(() => {
        this.reload();
        this.getProblemInfo("jump", index);
        this.reload();
      });
    },
    async submitAnswers() {
      var submitAnsList = JSON.parse(JSON.stringify(this.ansList));
      for (var i = 0; i < this.questionList.length; i++) {
        if (submitAnsList[i] == "" || submitAnsList[i] == []) {
          this.$message({
            message: "您尚未填写第" + (i + 1).toString() + "题！",
            type: "error",
          });
          return false;
        }
        if (
          this.questionList[i]["questionType"] == 0 ||
          this.questionList[i]["questionType"] == 1
        ) {
          //如果题目是选择题先转换形式
          var tempAns = "";
          for (var j = 0; j < submitAnsList[i].length; j++) {
            if (submitAnsList[i][j]["selected"]) {
              tempAns += submitAnsList[i][j]["name"];
            }
          }
          submitAnsList[i] = tempAns;
        }
        if (!this.questionList[i]["mustDo"] && submitAnsList[i] == "") {
          //如果该题目不是必做且用户没做
          continue;
        }
        if (
          this.questionList[i]["questionType"] == 0 ||
          this.questionList[i]["questionType"] == 1
        ) {
          //如果题目是选择题
          if (submitAnsList[i].length > this.questionList[i]["maxOptionNum"]) {
            this.$message({
              message: "您的第" + (i + 1).toString() + "题选项过多！",
              type: "error",
            });
            return false;
          } else if (
            submitAnsList[i].length < this.questionList[i]["minOptionNum"]
          ) {
            this.$message({
              message: "您的第" + (i + 1).toString() + "题选项过少！",
              type: "error",
            });
            return false;
          }
        } else if (this.questionList[i]["questionType"] == 2) {
          //如果题目是填空题
          if (submitAnsList[i].length > this.questionList[i]["maxOptionNum"]) {
            this.$message({
              message: "您的第" + (i + 1).toString() + "题字数过多！",
              type: "error",
            });
            return false;
          } else if (
            submitAnsList[i].length < this.questionList[i]["minOptionNum"]
          ) {
            this.$message({
              message: "您的第" + (i + 1).toString() + "题字数过少！",
              type: "error",
            });
            return false;
          }
        } else if (this.questionList[i]["questionType"] == 3) {
          //如果题目是框图题
          var blankNumber = JSON.parse(submitAnsList[i]).length;
          var tempDict = this.questionList[i];

          if (blankNumber > tempDict["maxOptionNum"]) {
            this.$message({
              message: "您的第" + (i + 1).toString() + "题图框过多！",
              type: "error",
            });
            return false;
          } else if (blankNumber < tempDict["minOptionNum"]) {
            this.$message({
              message: "您的第" + (i + 1).toString() + "题图框过少！",
              type: "error",
            });
            return false;
          }
        }
      }
      this.stateList[this.currentIndex]["state"] = true;
      this.isFinished = true;
      // 判断是否所有题目都做完了
      for (var stateItem of this.stateList) {
        if (!stateItem["state"]) {
          this.isFinished = false;
          break;
        }
      }
      axios
        .post("http://101.42.118.80:8000/submit_answer/", {
          username: this.username,
          taskId: this.taskId,
          ansList: submitAnsList,
          isFinished: this.isFinished,
        })
        .then((res) => {
          this.$message({
            type: "success",
            message: "提交成功!",
          });
          if (this.isFinished) {
            if (res.data["taskOver"]) {
              this.taskOverDialogVisible = true;
              return;
            }
            if (this.isTest) {
              this.passTest = res.data["passTest"];
              if (this.passTest) {
                this.getProblemInfo("next");
              }
              this.percentage =
                Math.round(res.data["testCorrectRate"] * 10000) / 100 + "%";
              this.testResultDialogVisible = true;
            } else {
              this.finalSubmitDialogVisible = true;
            }
          } else {
            this.reload();
            this.getProblemInfo("next");
            this.reload();
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
    async quitPerform() {
      if (this.initAnsListStr != JSON.stringify(this.ansList)) {
        await this.$confirm("请问是否需要提交当前答案？", "提示", {
          confirmButtonText: "确定",
          cancelButtonText: "取消",
          type: "warning",
        })
          .then(() => {
            if (!this.submitAnswers()) {
              return;
            }
          })
          .catch(() => {});
      }

      this.$router.push({
        name: "mine",
        query: {
          defaultActive: "1",
        },
      });
    },
    base64ImgtoFile(dataurl, filename = "file") {
      const arr = dataurl.split(",");
      const mime = arr[0].match(/:(.*?);/)[1];
      const suffix = mime.split("/")[1];
      const bstr = atob(arr[1]);
      let n = bstr.length;
      const u8arr = new Uint8Array(n);
      while (n--) {
        u8arr[n] = bstr.charCodeAt(n);
      }
      return new File([u8arr], `${filename}.${suffix}`, {
        type: mime,
      });
    },
    clickFillBlank(targetIndex, min, max, questionIndex) {
      this.imageLoading = true;
      this.fillBlankDialogVisible = true;
      this.currentImageSrc =
        "http://101.42.118.80:8000" +
        this.materialList[targetIndex]["filePath"].substr(1);
      this.imageLoading = false;

      this.currentMax = max;
      this.currentMin = min;

      if (this.ansList[questionIndex] == "") {
        this.initRects = [];
      } else {
        this.initRects = JSON.parse(this.ansList[questionIndex]);
      }
      return;
    },
    getFillBlankAns() {
      this.fillBlankDialogVisible = false;
      var tempAnsList = this.$refs.MyImageFramer.frameRects;

      for (var rect of tempAnsList) {
        rect.startX = Math.round(rect.startX);
        rect.startY = Math.round(rect.startY);
        rect.width = Math.round(rect.width);
        rect.height = Math.round(rect.height);
      }
      this.ansList[this.currentQuestionIndex] = JSON.stringify(tempAnsList);
    },
    getDeletedRow(selection, questionIndex) {
      //删除项目，由于需要前后对比才能知道删除了哪一项所以需要涉及到judgeList
      var judgeList = JSON.parse(JSON.stringify(this.ansList[questionIndex]));
      for (var tempRow of selection) {
        var tempTarget = tempRow["index"];
        judgeList[tempTarget]["selected"] = 0;
      }
      var targetIndex = -1;
      for (var tempRow of judgeList) {
        if (tempRow["selected"]) {
          targetIndex = tempRow["index"];
        }
      }

      for (var tempRow of this.lastSelectedList[questionIndex]) {
        if (tempRow["index"] == targetIndex) {
          return tempRow;
        }
      }
      return;
    },
    handleSelectionChange(selection, minOptionNum, maxOptionNum, index) {
      // section 被选中状态修改后触发事件，根据被选择的数量控制是否还可被选中
      if (this.initingSelection) {
        return;
      }

      if (selection.length > maxOptionNum) {
        // 如果这个题是单选
        if (minOptionNum == 1 && maxOptionNum == 1) {
          for (var tempRow of this.ansList[index]) {
            tempRow["selected"] = 0;
          }

          this.ansList[index][selection[1]["index"]]["selected"] = 1;
          this.$refs.regTable[index].toggleRowSelection(selection[0], false);
          return;
        }
        this.$message.warning(`最多只能选${maxOptionNum}条！`);
        this.$refs.regTable[index].toggleRowSelection(
          selection[selection.length - 1],
          false
        );
        return;
      }
      var lastLen = 0;
      for (var tempRow of this.ansList[index]) {
        if (tempRow["selected"]) {
          lastLen++;
        }
      }
      if (
        selection.length < minOptionNum &&
        selection.length < lastLen &&
        minOptionNum < maxOptionNum
      ) {
        this.$message.warning(`最少需要选${minOptionNum}条！`);
      }
      for (var tempRow of this.ansList[index]) {
        tempRow["selected"] = 0;
      }
      for (var tempRow of selection) {
        this.ansList[index][tempRow["index"]]["selected"] = 1;
      }
      this.lastSelectedList[index] = selection;
    },
  },
};
</script>

<style scoped>
/* 隐藏多选框 */
.selection-table /deep/ .el-table__header-wrapper .el-checkbox {
  display: none;
}

.header-style {
  border-radius: 5px;
  box-shadow: 2px 2px 8px 0 rgba(0, 0, 0, 0.315);
  height: 100px;
  padding: 20px 20px 20px 40px;
}

.header-breadcrumb {
  margin: 0 0 10px 0;
}

.header-title {
  float: left;
  font-size: 15px;
  font-weight: bold;
}

.main-style-two {
  padding: 20px 20px 20px 20px;
  border-radius: 5px;
  box-shadow: 2px 2px 8px 0 rgba(0, 0, 0, 0.315);
}

.main-style {
  padding: 20px 20px 20px 20px;
  margin-top: 20px;
  border-radius: 5px;
  box-shadow: 2px 2px 8px 0 rgba(0, 0, 0, 0.315);
}

.question-row {
  margin-top: 10px;
  border-top: 1px dashed #999999;
  padding-top: 10px;
}

.material-row {
  margin-top: 20px;
}

::-webkit-scrollbar {
  width: 10px;
  /*对垂直流动条有效*/
}

/*定义滚动条的轨道颜色、内阴影及圆角*/
::-webkit-scrollbar-track {
  border-radius: 4px;
}

/*定义滑块颜色、内阴影及圆角*/
::-webkit-scrollbar-thumb {
  border-radius: 8px;
  background-color: #efefef;
}

/*定义滑块悬停变化颜色、内阴影及圆角*/
::-webkit-scrollbar-thumb:hover {
  background-color: #dddddd;
}
.jump-logo {
  z-index: 2;
  animation: jump-logo 1s infinite;
  animation-timing-function: ease;
}
.jump-shadow {
  z-index: 1;
  width: 100px;
  height: 5px;
  background: #eaeaea;
  border-radius: 100%;
  animation: shadow 1s infinite;
  animation-timing-function: ease;
  margin-left: auto;
  margin-right: auto;
}
@keyframes jump-logo {
  0% {
    margin-bottom: 0px;
  }

  50% {
    margin-bottom: 30px;
  }

  100% {
    margin-bottom: 0px;
  }
}
@keyframes shadow {
  0% {
    width: 85px;
  }

  50% {
    width: 65px;
  }

  100% {
    width: 85px;
  }
}
</style>
